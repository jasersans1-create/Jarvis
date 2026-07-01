# Jarvis

A local voice assistant I built that runs on Linux.( its an Arch Linux package in the latest release right now , Runs currently on CLI)

It listens for **"Jarvis"**, understands voice commands, talks back using Piper TTS, remembers things locally, can generate code, launch apps, and control music.

Most speech runs online through the Hack Club AI API, but speech recognition automatically falls back to Vosk if you're offline.

---

## Features

- Wake word ("Jarvis")
- Natural voice conversations
- Offline Piper text-to-speech
- Offline Vosk speech recognition fallback
- Local memory (`memory.json`)
- Generate Python programs and open them in VS Code
- Launch common desktop apps
- Music playback controls

---

## Installation

Clone the repository.

```bash
git clone https://github.com/jasersans1-create/Jarvis.git
cd Jarvis
```

Create a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

Install Python packages.

```bash
pip install -r requirements.txt
```

Install system packages.

### Arch

```bash
sudo pacman -S portaudio ffmpeg
```

### Ubuntu/Debian

```bash
sudo apt install portaudio19-dev ffmpeg
```

Download a Piper voice.

```bash
mkdir -p tts

wget -O tts/en_US-hfc_male-medium.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx"

wget -O tts/en_US-hfc_male-medium.onnx.json \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx.json"
```

Copy the example environment file.

```bash
cp .env.example .env
```

Run it.

```bash
python main.py
```

---

## Using Jarvis

Wake it up by saying:

```
Jarvis
```

Examples:

```
Jarvis, remember I use dark mode.

Jarvis, open VS Code.

Jarvis, code a BMI calculator.

Jarvis, play music.
```

Say **sleep**, **exit**, or **goodbye** to go back to wake-word mode.

---

## Configuration

Everything is configured through `.env`.

Most people won't need to change anything except maybe:

- microphone device
- Piper model path
- Vosk model path
- preferred AI model

---

## Project layout

```
audio/      Voice input/output
brain/      Wake word, memory and intent matching
tools/      App launching, code generation and utilities
generated/  Generated code
tts/        Piper voice
vosk-model/ Offline speech model
```

---

## Notes

- Speech synthesis runs completely offline using Piper.
- If the internet goes down, speech recognition switches to Vosk automatically.
- Chat responses are generated through the Hack Club AI API OR THE KEY CAN BE USED SEPERATELY AS PER UR CHOICE.

---


Built by **Chirayu**
