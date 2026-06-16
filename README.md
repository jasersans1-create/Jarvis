# Jarvis — AI Voice Assistant

A local AI voice assistant powered by the **[AI Hack Club API](https://ai.hackclub.com)**.  
Say **"Jarvis"** to wake it up, then talk naturally.

---

## Features

| Feature | Description |
|---|---|
| 🎤 Wake Word | Say "Jarvis" to activate the assistant. |
| 💻 Code Generation | Ask Jarvis to write Python code, which opens automatically in VS Code. |
| 🎵 Music Control | Play, pause, skip, and go back through songs using keyboard hotkeys. |
| 🚀 App Launcher | Open Chrome, VS Code, Terminal, OBS, Minecraft, etc. |
| 🧠 Local Memory | Jarvis remembers and recalls facts locally in `memory.json`. |
| 🔊 Offline TTS | Speech synthesis with Piper TTS running completely locally. |
| 📴 Offline STT Fallback | Speech recognition automatically falls back offline using a local Vosk model when internet is down. |

---

## Quick Start (Under 5 Minutes)

### 1. Clone the repository

```bash
git clone https://github.com/jasersans1-create/Jarvis.git
cd Jarvis
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install system dependencies

Jarvis needs **ffmpeg** for audio playback and **portaudio** for microphone input.

**Arch Linux:**
```bash
sudo pacman -S portaudio ffmpeg
```

**Ubuntu / Debian:**
```bash
sudo apt install portaudio19-dev ffmpeg
```

**Fedora:**
```bash
sudo dnf install portaudio-devel ffmpeg
```

**macOS:**
```bash
brew install portaudio ffmpeg
```

### 5. Download a Piper voice model

Jarvis uses [Piper TTS](https://github.com/rhasspy/piper) for offline speech synthesis.  
Download a voice model from [Hugging Face](https://huggingface.co/rhasspy/piper-voices):

```bash
# Download a default US English voice model and config
mkdir -p tts
wget -O tts/en_US-hfc_male-medium.onnx \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx"
wget -O tts/en_US-hfc_male-medium.onnx.json \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx.json"
```

### 6. Configure environment

```bash
cp .env.example .env
```

The default `.env` works out of the box — no API key is needed. See [Configuration](#configuration) for all options.

### 7. Run

```bash
python main.py
```

Jarvis will say **"Jarvis is now online"** and start listening.

---
## OR FOR APP FROM RELEASAS DO:
### After downloading release from relasess:
``` bash
cd Downloads/
tar -xvzf jarvis-linux.tar.gz
chmod +x jarvis
./jarvis
```


## How It Works

### Wake Word

Jarvis listens for the word **"Jarvis"** (or common mishearings: "Jarvish", "Jervis", "Jarv").

```
You:     Jarvis
Jarvis:  Yes?
```

Once in conversation mode, you don't need to say "Jarvis" before every message.  
Say **"sleep"**, **"goodbye"**, or **"exit"** to return to wake-word mode.


### Memory

Jarvis can remember facts locally in `memory.json`:

```
You:     remember I prefer dark mode
Jarvis:  Okay. I'll remember that.

You:     what do you remember
Jarvis:  I remember: I prefer dark mode
```

### Code Generation

```
You:     Jarvis code a BMI calculator
Jarvis:  Building...
Jarvis:  Done. Saved to generated/bmi_calculator.py
```

Generated files are saved to the `generated/` folder and opened in VS Code automatically.

### Music Control

```
You:     Jarvis play music         → opens playlist in browser
You:     Jarvis next song          → skips to the next track
You:     Jarvis pause music        → pauses music playback
You:     Jarvis resume music       → resumes music playback
```

---

## AI Hack Club API

Jarvis is integrated with the **[AI Hack Club API](https://ai.hackclub.com)** — a free, OpenAI-compatible AI API for Hack Club members.

- **Endpoint:** `https://ai.hackclub.com/proxy/v1`
- **Authentication:** No API key required (optionally configure `HACKCLUB_AI_API_KEY` if key-based access is active)
- **Compatibility:** Fully compatible with standard OpenAI SDKs — just swap the `base_url`
- **Models:** Access to 30+ models including `qwen/qwen3-32b`, `google/gemini-2.5-flash`, `gpt-5-mini`, and more.

The integration is implemented using the standard `openai` library:

```python
from openai import OpenAI

client = OpenAI(
    api_key="not-needed",
    base_url="https://ai.hackclub.com/proxy/v1",
)

response = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

---

## Configuration

All settings are configured using environment variables. Copy `.env.example` to `.env` and adjust:

| Variable | Default | Description |
|---|---|---|
| `HACKCLUB_AI_BASE_URL` | `https://ai.hackclub.com/proxy/v1` | AI Hack Club API proxy endpoint |
| `HACKCLUB_AI_API_KEY` | `not-needed` | API key (not currently required) |
| `JARVIS_CHAT_MODEL` | `qwen/qwen3-32b` | Model for general conversation |
| `JARVIS_CODE_MODEL` | `qwen/qwen3-32b` | Model for code generation |
| `JARVIS_PIPER_BIN` | auto-detected | Path to piper binary |
| `JARVIS_VOICE_MODEL` | auto-detected | Path to `.onnx` voice model |
| `JARVIS_TTS_TMPFILE` | user temp folder | Path for temporary TTS wav file |
| `JARVIS_MIC_INDEX` | system default | Microphone device index |
| `JARVIS_RECORD_SECONDS` | `8` | Recording duration in seconds |
| `JARVIS_STT_OFFLINE` | `false` | Force offline STT using Vosk |
| `JARVIS_VOSK_MODEL` | `./vosk-model/` | Path to Vosk model for offline STT |
| `JARVIS_MUSIC_PLAYLIST` | lofi radio | YouTube URL opened by "play music" |
| `JARVIS_BROWSER` | auto-detected | Browser command |
| `JARVIS_WORKSPACES_DIR` | `~/Workspaces` | Directory for workspaces |
| `JARVIS_GENERATED_DIR` | `./generated` | Directory for generated code |

---

## Project Structure

```
Jarvis/
├── main.py              ← Assistant entry point
├── .env                 ← Your local configuration (not committed)
├── .env.example         ← Configuration template
├── requirements.txt     ← Python dependencies
├── memory.json          ← Local memory store (auto-created)
│
├── audio/
│   ├── listen.py        ← Audio input & online/offline speech recognition
│   └── speak.py         ← Audio output (Piper TTS)
│
├── brain/
│   ├── intents.py       ← Intent phrase definitions
│   ├── match.py         ← Intent matching logic
│   ├── memory.py        ← Memory read/write
│   ├── normalize.py     ← Centralized text normalization
│   └── wake.py          ← Wake word extractor
│
├── tools/
│   ├── apps.py          ← Desktop application launcher
│   ├── audio_mode.py    ← Microphone enable/disable state
│   ├── build.py         ← Code generator workspace management
│   ├── chat.py          ← AI conversation handler
│   ├── coder.py         ← Code generation handler
│   ├── files.py         ← Workspace file explorer integration
│   ├── music.py         ← Browser-based music playback control
│   └── workspace.py     ← Project workspace initializer
│
├── tts/                 ← Default location for Piper voice model
├── vosk-model/          ← Default location for Vosk speech model
└── generated/           ← Default directory for generated code
```

---

## Troubleshooting

**No speech recognized:**
- Ensure the microphone is connected and unmuted.
- Set `JARVIS_MIC_INDEX` to the correct device index.
- List available audio devices: `python -c "import sounddevice; print(sounddevice.query_devices())"`

**Piper TTS not working:**
- Verify `piper-tts` is installed in your virtual environment: `pip install piper-tts`.
- Set `JARVIS_PIPER_BIN` to the absolute path of the `piper` executable.

**Offline fallback issues:**
- If you lose internet and speech recognition stops working, make sure the local Vosk model is downloaded to `./vosk-model/vosk-model-small-en-us-0.15` and the `vosk` Python library is installed.

**API connection errors:**
- Check your internet connection.
- Verify `https://ai.hackclub.com` is online in your browser.

---

## License

MIT License — free to use, modify, and distribute.

# BUILT BY:
## CHIRAYU
