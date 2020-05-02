"""Define the application entrypoint."""
import importlib.util
import json
import logging
from pathlib import Path
import sys

from loguru import logger
from terraformpy import TFObject
import typer

from tfpy.core.stack import StackVars


app = typer.Typer()

# Configure logger.
INITIAL_LOG_LEVEL = logging.WARNING
LOG_FORMAT_COMPACT = "<level>{message}</level>"
LOG_FORMAT_VERBOSE = (
    "<level>{time:YYYY-MM-DDTHH:mm:ssZZ} {name}:{line:<4} {message}</level>"
)

# Remove any predefined logger.
logger.remove()

# Set the log colors.
logger.level("ERROR", color="<red><bold>")
logger.level("WARNING", color="<yellow>")
logger.level("SUCCESS", color="<green>")
logger.level("INFO", color="<cyan>")
logger.level("DEBUG", color="<blue>")
logger.level("TRACE", color="<magenta>")

# pylint: disable=C0330
@app.command()
def generate(
    project: str,
    environment: str = "",
    verbose: int = typer.Option(0, "--verbose", "-v", count=True),
):
    """Generate Terraform stacks."""
    # Configure logger verbosity .
    log_level = max(INITIAL_LOG_LEVEL - verbose * 10, 0)
    log_format = LOG_FORMAT_VERBOSE if log_level < logging.INFO else LOG_FORMAT_COMPACT
    logger.add(sys.stderr, format=log_format, level=log_level, colorize=True)

    # Load the stackvars.
    stackvars = StackVars(project, environment=environment, var_dir=Path.cwd(),)
    stackvars.load()
    # print(json.dumps(stackvars.vars, indent=4, sort_keys=True))

    # Import the libraries.
    library = Path("library")
    for lib in library.glob("**/*.py"):
        # Import the libs.
        logger.debug(f'Importing library "{lib}".')
        spec = importlib.util.spec_from_file_location(lib.stem, lib)
        module = importlib.util.module_from_spec(spec)
        sys.modules[lib.stem] = module
        spec.loader.exec_module(module)

    # Get the project stacks.
    s = Path("stacks")
    for stack in s.glob(f"{project}/**/*.tf.py"):
        # Import the stack.
        logger.debug(f'Importing stack "{stack}".')
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
