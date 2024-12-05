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
def poetry_config() -> Path:
    """Ensure a poetry configuration exists."""
    config_path = Path("~/.config/pypoetry/config.toml")
    if not config_path.parent.exists():
        os.makedirs(config_path.parent, exist_ok=True)
    if not config_path.exists():
        open(config_path, "x").close()
    return config_path


def test_add_command(poetry_config: Path) -> None:
    """Execute and verify the add command."""
    application = Application()
    application.add(AddCommand())

    command = application.find("azure add")
    command_tester = CommandTester(command)
    command_tester.execute(
        "test https://pkgs.dev.azure.com/test/_packaging/test/pypi/simple/",
    )


def test_config_command(poetry_config: Path) -> None:
    """Execute and verify the config command."""
    application = Application()
    application.add(ConfigCommand())

    command = application.find("azure config")
    command_tester = CommandTester(command)
    with pytest.raises(CleoMissingArgumentsError):
        command_tester.execute(
            "test"
        )
