"""Define the application entrypoint."""
import importlib.util
import json
import os
from pathlib import Path

import typer
from terraformpy import TFObject

from tfpy.core.stack import StackVars


app = typer.Typer()


@app.command()
def generate(stack: str, environment: str = ""):
    """Generate Terraform stacks."""
    # Load the stackvars.
    stackvars = StackVars(stack, environment=environment, var_dir=os.getcwd(),)
    stackvars.load()
    # print(json.dumps(stackvars.vars, indent=4, sort_keys=True))

    # Import the stack.
    spec = importlib.util.spec_from_file_location(stack, f"stacks/{stack}/main.tf.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Render it.
    render = getattr(module, "render")
    render(stackvars)
    tf_json = json.dumps(TFObject.compile(), indent=4, sort_keys=True)

    # Prepare the output file.
    p = Path(f"generated/{stack}")
    if environment:
        p = p / environment
    p.mkdir(parents=True, exist_ok=True)
    p = p / "main.tf.json"

    # Save the rendered stack to the file.
    p.write_text(tf_json)


if __name__ == "__main__":
    app()
