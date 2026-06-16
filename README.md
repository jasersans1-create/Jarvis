# Jarvis

A local AI voice assistant built in Python.

Wake it up with **"Jarvis"** and talk naturally.

Supports:

* Voice wake word
* Continuous conversation mode
* AI chat
* Memory
* Music control
* App launching
* Code generation
* Workspace management
* Natural offline speech

---

## Features

### Voice Assistant

* Wake word:

```
Jarvis
```

* Conversation mode:

```
Jarvis
→ chat normally
→ exit
→ sleep
```

No need to repeat the wake word every time.

---

### AI Chat

Ask things naturally:

```
Jarvis what is gravity
Jarvis explain differently
Jarvis help me code
```

Powered by:

* GPT API
* Memory context
* Conversational history

---

### Memory

Jarvis can remember information.

Examples:

```
remember I prefer Python
```

Recall:

```
what do you remember
```

Stored locally:

```
memory.json
```

---

### Code Generation

Examples:

```
Jarvis code a BMI calculator
Jarvis make a calculator
Jarvis build a hospital management system
```

Creates actual project files.

---

### Music Control

Commands:

```
play songs
pause music
resume music
next song
previous song
```

---

### Open Apps

Examples:

```
open chrome
open vscode
open minecraft
open terminal
open obs
```

---

## Tech Stack

Python

SpeechRecognition

OpenAI API

Piper TTS

FFmpeg

Systemd

VS Code

---

## Installation

Clone:

```bash
git clone YOUR_REPO_LINK
cd Jarvis
```

Create venv:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Add environment:

Create:

```
.env
```

Example:

```env
OPENAI_API_KEY=YOUR_KEY
```

Run:

```bash
python main.py
```

---

## Project Structure

```
Jarvis/

audio/
brain/
tools/
voices/

main.py
memory.json
.env
README.md
```

---

## Current Goals

* Better memory
* Faster responses
* Smarter actions
* Streaming speech
* Full desktop automation
* Better wake detection

---

## Example

User:

```
Jarvis
```

Jarvis:

```
Yes?
```

User:

```
Code a BMI calculator
```

Jarvis:

```
Done. Saved to project.
```

---

Built by Chirayu.
