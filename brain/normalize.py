"""
normalize.py — Text normalization helper for keyword extraction and matching.
"""

_REPLACEMENTS = {
    "vs code": "vscode",
    "visual studio code": "vscode",
    "git hub": "github",
    "mine craft": "minecraft",
    "obs studio": "obs",
    "vs": "vscode",
}


def normalize(text: str) -> str:
    """Lowercase and normalize common phrase variants."""
    text = text.lower()
    for old, new in _REPLACEMENTS.items():
        text = text.replace(old, new)
    return text.strip()