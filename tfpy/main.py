"""Define the application entrypoint."""
import os

import typer

from tfpy.core.stack import StackVars


app = typer.Typer()


@app.command()
def generate(stack: str, environment: str = ""):
    """Generate Terraform stacks."""
    _ = StackVars(stack, environment=environment, var_dir=os.getcwd(),)


if __name__ == "__main__":
    app()
