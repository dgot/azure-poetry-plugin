import re


def validate_url(index_url: str) -> None:
    """Validate index_url against the expected pattern.

    Parameters
    ----------
    idnex_url : str
        The URL to validate.

    Raises
    ------
    ValueError
        If the URL does not match the required pattern.

    Notes
    -----
    The required URL format is:
    `https://pkgs.dev.azure.com/{organization}/_packaging/{feed_name}/pypi/simple/`

    - `{organization}`: Must consist of letters, numbers, underscores, and hyphens.
    - `{feed_name}`: Must consist of letters, numbers, underscores, and hyphens.

    """  # noqa: E501
    url_pattern = re.compile(
        r"^https://pkgs\.dev\.azure\.com/"
        r"(?P<organization>[a-zA-Z0-9_-]+)/"
        r"_packaging/"
        r"(?P<feed_name>[a-zA-Z0-9_-]+)/"
        r"pypi/simple/$"
    )
    if not url_pattern.match(index_url):
        raise ValueError(
            "Invalid Index URL. The Index URL must match the pattern:\n"
            "https://pkgs.dev.azure.com/{organization}/_packaging/{feed_name}/pypi/simple/\n"
            "Where:\n"
            "- {organization} can contain letters, numbers, underscores, and hyphens.\n"  # noqa: E501
            "- {feed_name} can contain letters, numbers, underscores, and hyphens."  # noqa: E501
        )
