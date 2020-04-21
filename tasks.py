import os
from pathlib import Path

from invoke import task

PROJECT = Path(".").absolute().name


@task
def format(c, write=False):
    """Format the codebase."""
    write_or_diff = "" if write else "--check"
    c.run(f"black {write_or_diff} .")


@task
def lint(c):
    """Lint the codebase."""
    c.run(f"pylint {PROJECT}")
    c.run(f"flake8 {PROJECT}")


@task
def check(c):
    """Run the static analyzers."""
    c.run(f"pydocstyle {PROJECT}")


@task
def docs(c):
    """Build the documentation."""
    with c.cd("docs"):
        c.run("make html")


@task
def test(c):
    """Run the unit tests."""
    test_report_dir = os.environ.get("CIRCLE_TEST_REPORTS", "/tmp")
    c.run(
        "pytest -x "
        f"--junitxml={test_report_dir}/pytest/junit.xml "
        "--cov-report term-missing "
        "--cov-report html "
        f"--cov={PROJECT} "
        "tests"
    )


@task(format, lint, check, docs, test)
def ci(c):
    """Run all the CI tasks at once."""


@task
def publish_packages(c):
    """Publish packages on our internal PyPI."""
    c.run(
        "poetry publish --repository shipstation "
        f"--password {os.environ.get('GITHUB_TOKEN')}"
    )
