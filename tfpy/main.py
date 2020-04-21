import importlib.util
import os

import typer

from tfpy.core.stack import StackVars


app = typer.Typer()


@app.command()
def generate(stack: str, environment: str = ""):
    stackvars = StackVars(stack, environment=environment, var_dir=os.getcwd(),)


if __name__ == "__main__":
    app()
