from cleo.commands.command import Command
from cleo.helpers import argument
from poetry.config.config import Config

from azure_poetry_plugin.credentials import set_access_token


class ConfigCommand(Command):
    """Configure authentication for an Azure Artifact Feed.

    azure config
        {name} : Name the feed was added with.}
        {username : Username to authenticate as.}

    """

    name = "azure config"
    description = "Configure authentication for an Azure Artifact Feed."
    arguments = [
        argument(
            "name",
            description="Name the feed was added with.",
            optional=False,
        ),
        argument(
            "username",
            description="Username to authenticate as.",
            optional=False,
        )
    ]

    def handle(self) -> int:
        """Handle the config command."""
        config = Config.create()
        name = self.argument("name")
        username = self.argument("username")

        if not config.get("azure-devops", {}).get(name):
            self.write(
                f"<error>No artifact feed exists with the name: {name}</error>"
            )
            return 1

        access_token = self.secret(
            "Please provide an access token:"
        )
        if not isinstance(access_token, str):
            raise ValueError(
                "Access token cannot be a number. It must be a string"
            )
        set_access_token(
            repo_name=name,
            username=username,
            password=access_token,
            config=config,
        )
        return 0
