from tools.apps import (
    open_vscode,
    open_terminal,
    open_chrome
)

from tools.files import (
    open_project
)
from pathlib import Path
from brain.memory import remember


def run(name, func):

    print()

    print("Running:", name)

    try:

        result = func()

        print("Result:", result)

    except Exception as e:

        print("FAILED")

        print(e)

    print()


def start_coding():

    run(
        "terminal",
        open_terminal
    )

    run(
        "vscode",
        open_vscode
    )

    run(
        "project",
        open_project
    )

    run(
        "chrome",
        open_chrome
    )

    return True

BASE = "/home/chirayu"

def set_workspace(name):

    folder = (
        Path(BASE)
        / name
    )

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    remember(
        "workspace",
        str(folder)
    )

    return str(folder)