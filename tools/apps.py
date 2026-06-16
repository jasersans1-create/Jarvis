import shutil
import subprocess


def _launch(candidates):
    for cmd in candidates:
        if shutil.which(cmd[0]):
            subprocess.Popen(cmd)
            return True
    return False


def open_vscode():
    return _launch([
        ["code"]
    ])


def open_chrome():
    return _launch([
        ["google-chrome-stable"],
        ["google-chrome"],
        ["chromium"],
        ["chromium-browser"],
    ])


def open_minecraft():
    return _launch([
        ["sklauncher"],
    ])


def open_obs():
    return _launch([
        ["obs"],
    ])


def open_terminal():
    return _launch([
        ["kitty"],
        ["alacritty"],
        ["konsole"],
        ["gnome-terminal"],
        ["xfce4-terminal"],
        ["xterm"],
    ])