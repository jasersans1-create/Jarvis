"""
main.py — Jarvis AI Voice Assistant entry point.

Usage:
  python main.py

Jarvis listens for the wake word "Jarvis", then enters conversation mode.
Say "exit", "goodbye", or "sleep" to return to wake-word mode.

All configuration is done via environment variables. See .env.example.
"""

from audio.listen import listen
from audio.speak import speak
from brain.match import get_intent
from brain.wake import extract_command
from tools.chat import ask_chat

from tools.apps import (
    open_chrome,
    open_minecraft,
    open_obs,
    open_terminal,
    open_vscode,
)
from tools.workspace import start_coding, set_workspace
from tools.music import (
    play_music,
    next_song,
    previous_song,
    pause_song,
    resume_song,
)
from tools.build import build_code
from tools.audio_mode import enable_mic


# Maps intent names to handler functions
COMMANDS = {
    "open_chrome": open_chrome,
    "open_minecraft": open_minecraft,
    "open_obs": open_obs,
    "open_terminal": open_terminal,
    "open_vscode": open_vscode,
    "start_coding": start_coding,
    "play_music": play_music,
    "next_song": next_song,
    "previous_song": previous_song,
    "pause_music": pause_song,
    "resume_music": resume_song,
}

# Human-readable names for intent responses
NAMES = {
    "open_chrome": "Google Chrome",
    "open_minecraft": "Minecraft",
    "open_obs": "OBS Studio",
    "open_terminal": "Terminal",
    "open_vscode": "Visual Studio Code",
    "start_coding": "Project",
    "play_music": "Music",
    "next_song": "Next Song",
    "previous_song": "Previous Song",
    "pause_music": "Pause",
    "resume_music": "Resume",
}

_EXIT_COMMANDS = {"exit", "goodbye", "sleep", "go to sleep", "bye"}


def main() -> None:
    chat_mode = False

    speak("Jarvis is now online")
    print("[JARVIS] Ready. Say 'Jarvis' to begin.")

    while True:
        print("[JARVIS] Listening...")
        text = listen()

        if not text:
            continue

        print(f"[JARVIS] Heard: {text!r}")

        # ── Wake word mode ───────────────────────────────────────────
        if not chat_mode:
            command = extract_command(text)

            if command is None:
                # Wake word not detected
                continue

            if command == "":
                # Wake word only — enter chat mode
                speak("Yes?")
                chat_mode = True
                continue

        # ── Chat mode ────────────────────────────────────────────────
        else:
            command = text.lower().strip()

        print(f"[JARVIS] Command: {command!r}")

        # Exit / sleep
        if command in _EXIT_COMMANDS:
            speak("Alright. Going back to sleep.")
            chat_mode = False
            continue

        intent = get_intent(command)
        print(f"[JARVIS] Intent: {intent}")

        # Code generation
        if intent == "make_code":
            speak("Building...")
            file_path = build_code(command)
            speak(f"Done. Saved to {file_path}")
            chat_mode = True

        # Set workspace folder
        elif intent == "set_workspace":
            speak("What should I call this workspace?")
            name_text = listen()
            if name_text:
                folder = set_workspace(name_text.strip())
                speak(f"Workspace set to {folder}")
            else:
                speak("I didn't catch a name. Try again.")
            chat_mode = True

        # Known app / system command
        elif intent in COMMANDS:
            name = NAMES.get(intent, intent.replace("_", " ").title())
            speak(f"Opening {name}")
            COMMANDS[intent]()
            chat_mode = True

        # Fall through to AI chat
        else:
            reply = ask_chat(command)
            speak(reply)
            chat_mode = True


if __name__ == "__main__":
    main()