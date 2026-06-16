from brain.intents import INTENTS


def normalize(text):

    text = text.lower()

    replacements = {

        "vs code": "vscode",

        "visual studio code": "vscode",

        "mine craft": "minecraft",

        "obs studio": "obs"

    }

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )

    return text.strip()


def get_intent(text):

    text = normalize(text)

    print("TEXT =", text)

    for intent in INTENTS:

        phrases = INTENTS[intent]

        for phrase in phrases:

            phrase = normalize(
                phrase
            )

            print(
                "checking",
                phrase
            )

            if phrase in text:

                return intent

    return None