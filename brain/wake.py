def extract_command(text: str):

    if not text:
        return None

    text = text.lower().strip()

    WAKE_WORDS = [

        "jarvis",

        "javed",

        "jarvish",

        "jervis",

        "jarv",

        "java"
    ]

    wake = None

    for word in WAKE_WORDS:

        if word in text:

            wake = word
            break

    if wake is None:
        return None

    command = (
        text
        .replace(wake, "", 1)
        .strip()
    )

    command = command.lstrip(
        " ,.!?:"
    )

    return command if command else ""