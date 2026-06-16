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

chat_mode = False

speak("Jarvis is now online")

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

while True:

    print(
        "Sleeping..."
    )

    text = listen()

    if not text:
        continue

    print(
        "Heard:",
        text
    )


    # NORMAL MODE
    if not chat_mode:

        command = extract_command(
            text
        )

        if command is None:
            continue


        if command == "":

            speak(
                "Yes?"
            )

            chat_mode = True

            continue


    # CHAT MODE
    else:

        command = text.lower()


    print(
        "Command:",
        command
    )


    if command in [

        "exit",
        "goodbye",
        "sleep",
        "go to sleep"

    ]:

        speak(
            "Alright. Going back to sleep."
        )

        chat_mode = False

        continue


    intent = get_intent(
        command
    )

    print(
        "Intent:",
        intent
    )


    if intent == "make_code":

        speak(
            "Building"
        )

        file = build_code(
            command
        )

        speak(
            f"Done. Saved to {file}"
        )

        chat_mode = True


    elif intent in COMMANDS:

        name = NAMES.get(

            intent,

            intent.replace(
                "_",
                " "
            ).title()

        )

        speak(

            f"Opening {name}"

        )

        COMMANDS[intent]()

        chat_mode = True
    else:

        reply = ask_chat(
            command
        )

        speak(
            reply
        )

        chat_mode = True