"""
workspace.py — Workspace and project management tools.

Environment variables:
  JARVIS_WORKSPACES_DIR — base directory for workspaces
                          (default: ~/Workspaces)
"""

import os
from pathlib import Path

from tools.apps import open_vscode, open_terminal, open_chrome
from tools.files import open_project
from brain.memory import remember


# Base directory for all workspaces — configurable via env var
_WORKSPACES_BASE = Path(
    os.getenv("JARVIS_WORKSPACES_DIR", str(Path.home() / "Workspaces"))
)


def _run(name: str, func) -> None:
    """Run a function and log the result."""
    print()
    print(f"Running: {name}")
    try:
        result = func()
        print(f"Result: {result}")
    except Exception as e:
        print(f"FAILED: {e}")
    print()


def start_coding() -> bool:
    """Open all tools needed for a coding session."""
    _run("terminal", open_terminal)
    _run("vscode", open_vscode)
    _run("project", open_project)
    _run("chrome", open_chrome)
    return True


def set_workspace(name: str) -> str:
    """Create a named workspace folder and save it to memory."""
    folder = _WORKSPACES_BASE / name
    folder.mkdir(parents=True, exist_ok=True)
    remember("workspace", str(folder))
    return str(folder)