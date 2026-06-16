"""
memory.py — Local key-value memory store backed by memory.json.

The memory file is stored relative to the project root so it works
regardless of where Python is invoked from.
"""

import json
from pathlib import Path


# Store memory.json in the project root
_MEMORY_FILE = Path(__file__).resolve().parent.parent / "memory.json"


def load() -> dict:
    """Load and return all stored memories."""
    if not _MEMORY_FILE.exists():
        return {}
    try:
        with open(_MEMORY_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save(data: dict) -> None:
    """Persist the memory dictionary to disk."""
    with open(_MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def remember(key: str, value: str) -> None:
    """Store a key-value pair in memory."""
    data = load()
    data[key] = value
    save(data)


def recall(key: str) -> str | None:
    """Retrieve a value from memory by key."""
    return load().get(key)


def forget(key: str) -> bool:
    """Remove a key from memory. Returns True if key existed."""
    data = load()
    if key in data:
        del data[key]
        save(data)
        return True
    return False