install_pipx () {
    pip install --upgrade pip
    python3 -m pip install --user pipx
}

install_poetry () {
    pipx install poetry
}

install_project () {
    poetry install
}

install_pre_commit () {
    pipx install pre-commit
	pre-commit install --hook-type pre-commit --hook-type pre-push --overwrite
}

install_pipx
install_poetry
install_project
