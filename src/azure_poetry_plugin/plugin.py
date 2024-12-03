from poetry.config.config import Config
from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin

from azure_poetry_plugin.commands import COMMANDS, register_commands
from azure_poetry_plugin.repository import add_repository


def configure_azure_devops(application: Application) -> None:
    """Configure the peotry instance with the available artifact feeds."""
    poetry = application.poetry
    io = application.create_io()
    config = Config.create()

    azure_devops_config = config.get("azure-devops", {})
    if not azure_devops_config:
        return

    for repo_name, source in azure_devops_config.items():
        if not isinstance(source, dict):
            io.write_error(
                f"[azure-devops.{repo_name}] configuration is malformed."
            )
            continue
        if not source.get("url"):  # type: ignore
            io.write_error(
                f"[azure-devops.{repo_name}] is missing its 'url' key-value. "
                "You can fix this by adding it again with: \n"
                f"poetry azure add {repo_name} <url>."
            )
            continue
        if poetry.pool.has_repository(repo_name):
            continue
        add_repository(
            repo_name=repo_name,
            index_url=source["url"], # type: ignore
            poetry=poetry,
            config=config,
        )


class AzurePoetryPlugin(ApplicationPlugin):
    """Plugin supporting azure artifact feeds as private repositories."""

    _commands = COMMANDS

    def activate(self, application: Application) -> None:
        """Activate plugin on poetry invokation."""
        register_commands(application=application, commands=self._commands)
        configure_azure_devops(application=application)
