"""
files.py — Project file/folder management.
"""

import shutil
import subprocess

from brain.memory import recall


def open_project() -> bool:
    """Open the remembered project folder in VS Code."""
    path = recall("project")

    if not path:
        print("[JARVIS] No project path saved in memory.")
        return False

    import os
    if not os.path.isdir(path):
        print(f"[JARVIS] Project path does not exist: {path}")
        return False

    if not shutil.which("code"):
        print("[JARVIS] VS Code ('code') not found in PATH.")
        return False

    subprocess.Popen(["code", "--reuse-window", path])
    return True