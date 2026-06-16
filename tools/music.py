import subprocess
import pyautogui
import time
from tools.audio_mode import disable_mic


PLAYLIST = (
    "https://www.youtube.com/playlist?list=PLhsz9CILh357zA1yMT-K5T9ZTNEU6Fl6n&index=1"
)


def play_music():

    disable_mic()

    subprocess.Popen(
        [
            "google-chrome-stable",
            PLAYLIST
        ]
    )


def next_song():
    pyautogui.press("shift")
    pyautogui.press("n")


def previous_song():
    pyautogui.press("shift")
    pyautogui.press("p")


def pause_song():
    pyautogui.press("space")


def resume_song():
    pyautogui.press("space")