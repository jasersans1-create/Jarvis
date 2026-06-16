"""
music.py — Music playback control via browser and keyboard shortcuts.

Environment variables:
  JARVIS_MUSIC_PLAYLIST — YouTube playlist URL to open for music playback
  JARVIS_BROWSER        — browser command to use (default: auto-detect)
"""

import os
import subprocess
import shutil
import pyautogui

from tools.audio_mode import disable_mic


# Default playlist — override via environment variable
_PLAYLIST = os.getenv(
    "JARVIS_MUSIC_PLAYLIST",
    "https://www.youtube.com/watch?v=jfKfPfyJRdk",  # lofi hip hop radio (public)
)

# Browser to launch — override via environment variable
_BROWSER_OVERRIDE = os.getenv("JARVIS_BROWSER", "")


def _get_browser() -> list[str] | None:
    """Find an available browser command."""
    if _BROWSER_OVERRIDE and shutil.which(_BROWSER_OVERRIDE):
        return [_BROWSER_OVERRIDE]

    candidates = [
        "google-chrome-stable",
        "google-chrome",
        "chromium",
        "chromium-browser",
        "firefox",
        "xdg-open",
    ]
    for cmd in candidates:
        if shutil.which(cmd):
            return [cmd]
    return None


def play_music() -> None:
    """Open the music playlist in a browser."""
    disable_mic()

    browser = _get_browser()
    if not browser:
        print("[JARVIS] No browser found. Set JARVIS_BROWSER in .env")
        return

    subprocess.Popen(browser + [_PLAYLIST])


def next_song() -> None:
    """Skip to the next song (YouTube keyboard shortcut)."""
    pyautogui.hotkey("shift", "n")


def previous_song() -> None:
    """Go to the previous song (YouTube keyboard shortcut)."""
    pyautogui.hotkey("shift", "p")


def pause_song() -> None:
    """Pause playback (YouTube keyboard shortcut)."""
    pyautogui.press("space")


def resume_song() -> None:
    """Resume playback (YouTube keyboard shortcut)."""
    pyautogui.press("space")