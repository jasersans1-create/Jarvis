import re
import subprocess


def clean(text):

    text = re.sub(
        r"\*+",
        "",
        text
    )

    text = re.sub(
        r"`+",
        "",
        text
    )

    text = re.sub(
        r"#+",
        "",
        text
    )

    text = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        r"\1",
        text
    )

    text = re.sub(
        r"\n+",
        " ",
        text
    )

    return text.strip()


def speak(text):

    text = clean(text)

    print(
        "\n[JARVIS]"
    )

    print(
        text
    )
    subprocess.run(
    [
            "/home/chirayu/Jarvis/.venv/bin/piper",
            "--model",
            "/home/chirayu/Jarvis/voices/en_US-lessac-medium.onnx",
            "--output_file",
            "/tmp/jarvis.wav"
        ],
        input=text.encode()
    )
    subprocess.run(
        [
            "ffplay",
            "-nodisp",
            "-autoexit",
            "-loglevel",
            "quiet",
            "/tmp/jarvis.wav"
        ]
    )