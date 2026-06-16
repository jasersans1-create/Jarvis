import json
import os


FILE="memory.json"


def load():

    if not os.path.exists(
        FILE
    ):

        return {}

    with open(
        FILE
    ) as f:

        return json.load(
            f
        )


def save(data):

    with open(
        FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def remember(
    key,
    value
):

    data=load()

    data[
        key
    ]=value

    save(
        data
    )


def recall(
    key
):

    return load().get(
        key
    )