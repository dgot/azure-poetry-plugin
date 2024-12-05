import os
from pathlib import Path

import pytest
from cleo.application import Application
from cleo.exceptions import CleoMissingArgumentsError
from cleo.testers.command_tester import CommandTester

from azure_poetry_plugin.commands import (
    AddCommand,  # noqa: F401
    ConfigCommand,  # noqa: F401
)


@pytest.fixture(scope="session")
def _poetry_config() -> Path:
    """Ensure a poetry configuration exists."""
    import subprocess
    subprocess.run(
        ["poetry config repositories.baselifescience"],
        check=True,
    )


def test_add_command() -> None:
    """Execute and verify the add command."""
    application = Application()
    application.add(AddCommand())

    command = application.find("azure add")
    command_tester = CommandTester(command)
    command_tester.execute(
        "test https://pkgs.dev.azure.com/test/_packaging/test/pypi/simple/",
    )


def test_config_command() -> None:
    """Execute and verify the config command."""
    application = Application()
    application.add(ConfigCommand())

    command = application.find("azure config")
    command_tester = CommandTester(command)
    with pytest.raises(CleoMissingArgumentsError):
        command_tester.execute(
            "test"
        )
