from typing import Callable

from cleo.commands.command import Command
from poetry.console.application import Application

from azure_poetry_plugin.commands.add import AddCommand
from azure_poetry_plugin.commands.config import ConfigCommand

__all__ = [
    "AddCommand",
    "ConfigCommand",
]

COMMANDS: list[type[Command]] = [
    AddCommand,
    ConfigCommand,
]

def get_command_factory(command: type[Command]) -> Callable[[], Command]:
    """Wrap command in a factory.

    Wraps command type in a function, which initializes and returns said
    command when called. Used for deffered command initialization, as required
    by Poetry.
    """
    return lambda *args, **kwargs: command()  # type: ignore


def register_commands(
    application: Application,
    commands: list[type[Command]],
) -> None:
    """Register commands with a Poetry Application."""
    for command in commands:
        if command.name:
            application.command_loader.register_factory(
                command.name, get_command_factory(command)
            )
