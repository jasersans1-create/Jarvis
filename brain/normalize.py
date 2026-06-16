def normalize(text):

    text = text.lower()

    replacements = {
        "vs code": "vscode",
        "visual studio code": "vscode",
        "git hub": "github",
        "mine craft": "minecraft",
        "vs" : "vscode"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text