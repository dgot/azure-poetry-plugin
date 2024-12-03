from poetry.config.config import Config
from poetry.factory import Factory
from poetry.poetry import Poetry
from poetry.repositories.repository_pool import Priority


def add_repository(
    repo_name: str,
    index_url: str,
    poetry: Poetry,
    config: Config,
) -> None:
    """Add artifact feed as a repository to the current Poetry Session."""
    source = {
        "name": repo_name,
        "url": index_url,
    }
    repository = Factory.create_package_source(
        source=source,
        config=config,
        disable_cache=True,
    )
    poetry.pool.add_repository(
        repository=repository,
        priority=Priority.SUPPLEMENTAL,
        secondary=True,
    )
