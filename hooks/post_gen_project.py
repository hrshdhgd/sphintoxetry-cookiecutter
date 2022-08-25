"""Code to run after generating the project."""
from os.path import realpath, curdir
from os import rename
from pathlib import Path

PROJECT_DIRECTORY = Path(realpath(curdir)).resolve()
MODULE_NAME = "{{ cookiecutter.package_name }}"
MODULE_PATH = PROJECT_DIRECTORY.joinpath("src", MODULE_NAME)

if "-" in MODULE_NAME:
    NEW_MODULE_NAME = MODULE_NAME.replace("-", "_")
    NEW_MODULE_PATH = PROJECT_DIRECTORY.joinpath("src", NEW_MODULE_NAME)
    rename(MODULE_PATH, NEW_MODULE_PATH)
