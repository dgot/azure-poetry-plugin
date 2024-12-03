from cleo.commands.command import Command
from cleo.helpers import argument
from poetry.config.config import Config

from azure_poetry_plugin.utils import validate_url


class AddCommand(Command):
    """Add artifact feed to poetry as a globally available source.

    azure add
        {name} : Name to store the feed as}
        {index-url : URL to the artifact feed}
    """

    name = "azure add"
    description = "Add artifact feed to poetry as a globally available source."
    arguments = [
        argument(
            "name",
            description="Name to store the feed as",
            optional=False,
        ),
        argument(
            "index-url",
            description="URL for the artifact feed",
            optional=False,
        ),
    ]

    def handle(self) -> int:
        """Execute Add command."""
        config = Config.create()
        name = self.argument("name")
        index_url = self.argument("index-url")

        validate_url(index_url=index_url)

        azure_devops_config = config.get(f"azure-devops.{name}", {})
        if azure_devops_config:
            self.line(
                f"<info>An artifact feed with the name {name} already exists. "
                "Updating configuration.</info>"
            )
        azure_devops_config.update({ "url": index_url })
        # Persist the settings by adding the property to the config source.
        config.config_source.add_property(
            f"azure-devops.{name}", azure_devops_config
        )
        return 0
