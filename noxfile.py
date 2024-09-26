"""Nox for running build against different versions of Python.

This session performs the following steps:

Build a wheel from the local package.
Install the wheel as well as the pytest package.
Invoke pytest to run the test suite against the installation.

"""

from nox_poetry import session
from nox_poetry.sessions import Session


@session(python=[
    "3.9",
    "3.10",
    "3.11",
    "3.12",
])
def test(session: Session) -> None:
    """Run tests against project build."""
    session.install("pytest", ".")
    session.run("pytest")
