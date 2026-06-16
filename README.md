# Jarvis

Jarvis is a local AI voice assistant built in Python.

Wake it up with **"Jarvis"** and talk naturally using voice or text.

## Features

- Wake word detection
- Continuous conversation mode
- AI chat
- Local memory
- Music control
- App launching
- Code generation
- Workspace management
- Offline speech output

## Voice Assistant

Wake word:

```text
Jarvis

Conversation mode:

Jarvis
→ chat normally
→ say "sleep" to stop listening

You do not need to repeat the wake word for every message once conversation mode starts.

AI Chat

Ask things naturally:

Jarvis what is gravity
Jarvis explain recursion
Jarvis help me code

Jarvis uses:

OpenAI-compatible API
Conversation history
Local memory context
Memory

Jarvis can remember information locally.

Examples:

remember I prefer Python
what do you remember

Stored in:

memory.json
Code Generation

Examples:

Jarvis code a BMI calculator
Jarvis make a calculator
Jarvis build a hospital management system

Jarvis can generate project files and code scaffolds.

Music Control

Commands:

play songs
pause music
resume music
next song
previous song
Open Apps

Examples:

open chrome
open vscode
open minecraft
open terminal
open obs
Tech Stack
Python
SpeechRecognition
OpenAI-compatible API
Piper TTS
FFmpeg
Systemd
VS Code
Installation
1. Clone the repository
git clone https://github.com/jasersans1-create/Jarvis
cd Jarvis
2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Install system dependencies

Jarvis may also need some system packages for audio and GUI support.

Arch Linux
sudo pacman -S python python-pip tk portaudio ffmpeg
Ubuntu / Debian
sudo apt install python3 python3-pip python3-tk portaudio19-dev ffmpeg
Fedora
sudo dnf install python3 python3-pip python3-tkinter portaudio-devel ffmpeg
5. Set up environment variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here
JARVIS_NAME=User

You can also export the key temporarily in your terminal.

Linux / macOS
export OPENAI_API_KEY="your_api_key_here"
Windows PowerShell
setx OPENAI_API_KEY "your_api_key_here"
Run
python main.py
Project Structure
Jarvis/
├── audio/
├── brain/
├── tools/
├── tts/
├── voices/
├── wake/
├── main.py
├── memory.json
├── requirements.txt
├── README.md
└── .env
Configuration

Jarvis is designed to be portable.

Avoid hardcoding:

your name
absolute file paths
machine-specific folders

Use environment variables and relative paths instead.

Example:

from pathlib import Path
import os

BASE_DIR = Path(__file__).parent
USER_NAME = os.getenv("JARVIS_NAME", "User")
Current Goals
Better memory
Faster responses
Smarter actions
Streaming speech
Full desktop automation
Better wake detection
Example

User:

Jarvis

Jarvis:

Yes?

User:

Code a BMI calculator

Jarvis:

Done. Saved to project.
Notes
You must provide your own API key
Never commit .env
Some voice features depend on system audio libraries
Some features may require additional setup on Linux
Built by

Chirayu