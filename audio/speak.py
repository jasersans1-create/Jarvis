"""
speak.py — Text-to-speech output using Piper TTS and ffplay.

Piper TTS documentation: https://github.com/rhasspy/piper

Required system tools:
  - piper  (installed via pip as piper-tts, or as a system binary)
  - ffplay (part of ffmpeg)

Environment variables:
  JARVIS_PIPER_BIN   — path to the piper binary (default: auto-detect from venv)
  JARVIS_VOICE_MODEL — path to the .onnx voice model file
  JARVIS_TTS_TMPFILE — temp wav file path (default: /tmp/jarvis.wav)
"""

import re
import subprocess
import shutil
import os
import tempfile
import getpass
from pathlib import Path

# Locate piper binary: prefer venv, fall back to system PATH
_project_root = Path(__file__).resolve().parent.parent

def _find_piper() -> str:
    """Find the piper TTS binary."""
    # Allow override via environment variable
    env_bin = os.getenv("JARVIS_PIPER_BIN")
    if env_bin and shutil.which(env_bin):
        return env_bin

    # Check project virtualenv
    venv_piper = _project_root / ".venv" / "bin" / "piper"
    if venv_piper.exists():
        return str(venv_piper)

    # Fall back to system PATH
    system_piper = shutil.which("piper")
    if system_piper:
        return system_piper

    return "piper"  # Let it fail with a clear error


def _find_voice_model() -> str:
    """Find the voice model file."""
    env_model = os.getenv("JARVIS_VOICE_MODEL")
    if env_model:
        return env_model

    # Check default locations within project
    candidates = [
        _project_root / "tts" / "en_US-hfc_male-medium.onnx",
        _project_root / "voices" / "en_US-lessac-medium.onnx",
        _project_root / "voices" / "en_US-hfc_male-medium.onnx",
    ]
    for path in candidates:
        if path.exists():
            return str(path)

    return str(candidates[0])  # Will fail with a clear error if not found


_PIPER_BIN = _find_piper()
_VOICE_MODEL = _find_voice_model()

def _get_default_tmpfile() -> str:
    username = getpass.getuser()
    return str(Path(tempfile.gettempdir()) / f"jarvis_{username}.wav")

_TMP_WAV = os.getenv("JARVIS_TTS_TMPFILE", _get_default_tmpfile())


def clean(text: str) -> str:
    """Strip markdown formatting so spoken text sounds natural."""
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"`+", "", text)
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)
    text = re.sub(r"\n+", " ", text)
    return text.strip()


def _ensure_voice_config(model_path: str) -> None:
    """Ensure the .json config file for the voice model exists, download if missing."""
    model_path_obj = Path(model_path)
    json_path = model_path_obj.with_suffix(model_path_obj.suffix + ".json")
    
    if json_path.exists():
        return

    print(f"[JARVIS] Config file {json_path} is missing.")
    
    # Try to auto-download if it is the default model
    if model_path_obj.name == "en_US-hfc_male-medium.onnx":
        url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx.json"
        print(f"[JARVIS] Attempting to download default voice config from {url}...")
        try:
            import urllib.request
            json_path.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(url, str(json_path))
            print("[JARVIS] Voice config downloaded successfully.")
            return
        except Exception as e:
            print(f"[JARVIS] Failed to auto-download config: {e}")
            
    # Print error/help instructions if we couldn't resolve/download it
    print(f"\n[JARVIS] ERROR: Piper TTS requires a config JSON file alongside the ONNX model.")
    print(f"Please download the corresponding config file and place it at:")
    print(f"  {json_path}")
    print(f"\nExample command to download the default config:")
    print(f"  wget -O {json_path} \"https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx.json\"\n")


def speak(text: str) -> None:
    """Synthesize and play speech using Piper TTS + ffplay."""
    _ensure_voice_config(_VOICE_MODEL)
    text = clean(text)

    print("\n[JARVIS]")
    print(text)

    try:
        subprocess.run(
            [
                _PIPER_BIN,
                "--model", _VOICE_MODEL,
                "--output_file", _TMP_WAV,
            ],
            input=text.encode(),
            check=True,
        )
        subprocess.run(
            [
                "ffplay",
                "-nodisp",
                "-autoexit",
                "-loglevel", "quiet",
                _TMP_WAV,
            ],
            check=True,
        )
    except FileNotFoundError as e:
        print(f"[JARVIS] TTS error — missing binary: {e}")
        print(f"[JARVIS] Install piper-tts and ffmpeg, or set JARVIS_PIPER_BIN / JARVIS_VOICE_MODEL")
    except subprocess.CalledProcessError as e:
        print(f"[JARVIS] TTS error: {e}")