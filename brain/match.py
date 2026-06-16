"""
match.py — Intent recognition using keyword phrase matching.
"""

from brain.intents import INTENTS
from brain.normalize import normalize


def get_intent(text: str) -> str | None:
    """
    Match text against known intent phrases.
    Returns the intent name, or None if no match found.
    """
    normalized = normalize(text)

    for intent, phrases in INTENTS.items():
        for phrase in phrases:
            if normalize(phrase) in normalized:
                return intent

    return None