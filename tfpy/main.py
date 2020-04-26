"""Define the application entrypoint."""
import importlib.util
import json
from pathlib import Path
import sys

import typer
from terraformpy import TFObject

from tfpy.core.stack import StackVars


app = typer.Typer()


@app.command()
def generate(project: str, environment: str = ""):
    """Generate Terraform stacks."""
    # Load the stackvars.
    stackvars = StackVars(project, environment=environment, var_dir=Path.cwd(),)
    stackvars.load()
    # print(json.dumps(stackvars.vars, indent=4, sort_keys=True))

    # Import the libraries.
    library = Path("library")
    for lib in library.glob("**/*.py"):
        # Import the libs.
        spec = importlib.util.spec_from_file_location(lib.stem, lib)
        module = importlib.util.module_from_spec(spec)
        sys.modules[lib.stem] = module
        spec.loader.exec_module(module)

    # Get the project stacks.
    s = Path("stacks")
    for stack in s.glob("**/*.tf.py"):
        # Import the stack.
        spec = importlib.util.spec_from_file_location(
            stack.name.replace("".join(stack.suffixes), ""), stack
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Render it.
        render = getattr(module, "render")
        render(stackvars)

    # Compile them.
    tf_json = json.dumps(TFObject.compile(), indent=4, sort_keys=True)

    # Prepare the output file.
    p = Path(f"generated/{project}")
    if environment:
        p = p / environment
    p.mkdir(parents=True, exist_ok=True)
    p = p / "main.tf.json"

    # Save the rendered stack to the file.
    p.write_text(tf_json)


if __name__ == "__main__":
    app()
