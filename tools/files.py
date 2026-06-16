import subprocess
import os

from brain.memory import recall


def open_project():

    path = recall(
        "project"
    )

    print(
        "PROJECT:",
        path
    )

    if not path:
        return False


    if not os.path.isdir(
        path
    ):
        return False


    subprocess.Popen([

        "code",

        "--reuse-window",

        path

    ])

    return True