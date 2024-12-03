from typing import Dict, Union

from poetry.config.config import Config
from poetry.utils.password_manager import PasswordManager


def set_access_token(
    repo_name: str,
    username: str,
    password: str,
    config: Config,
) -> None:
    """Set access token with the poetry passwordmanager."""
    password_manager = PasswordManager(config=config)
    password_manager.set_http_password(
        repo_name=repo_name,
        username=username,
        password=password,
    )


def get_access_token(
    repo_name: str,
    config: Config,
) -> Union[Dict[str, Union[str, None]], None]:
    """Get access token with the poetry passwordmanager."""
    password_manager = PasswordManager(config=config)
    access_token = password_manager.get_http_auth(repo_name=repo_name)
    return access_token
