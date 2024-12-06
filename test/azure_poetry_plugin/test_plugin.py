import logging
import os
from pathlib import Path

import pytest
from cleo.application import Application
from cleo.exceptions import CleoMissingArgumentsError
from cleo.testers.command_tester import CommandTester
from poetry.config.config import CONFIG_DIR, Config

from azure_poetry_plugin.commands import (
    AddCommand,  # noqa: F401
    ConfigCommand,  # noqa: F401
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def poetry_config() -> Path:
    """Ensure a poetry configuration exists."""
    config = Config.create()
    config_file = Path(os.path.join(CONFIG_DIR, "config.toml"))
    if not config.config_source.file.exists():
        os.makedirs(CONFIG_DIR, exist_ok=True)
        try:
            open(config_file, "x").close()
        except FileExistsError:
            logger.warning(
                f"poetry configuration file at: {config_file} "
                "was created by another process."
            )
    return config_file


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
