install_pipx () {
    pip install --upgrade pip
    python3 -m pip install --user pipx
}

install_poetry () {
    pipx install poetry
}

install_pipx
install_poetry