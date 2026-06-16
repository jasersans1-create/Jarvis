"""
listen.py — Microphone input and speech recognition.

Uses sounddevice for audio capture, SpeechRecognition (Google) for online STT,
and Vosk for offline STT fallback.

Environment variables:
  JARVIS_MIC_INDEX      — microphone device index (default: system default)
  JARVIS_RECORD_SECONDS — how many seconds to record per utterance (default: 8)
  JARVIS_STT_OFFLINE    — force offline STT using Vosk (default: false)
  JARVIS_VOSK_MODEL     — path to Vosk model directory
                          (default: ./vosk-model/vosk-model-small-en-us-0.15)
"""

import os
import time
import json
from pathlib import Path

import numpy as np
import sounddevice as sd
import speech_recognition as sr

from tools.audio_mode import mic_enabled


# Read configuration from environment
_MIC_INDEX = None
_env_mic = os.getenv("JARVIS_MIC_INDEX")
if _env_mic is not None:
    try:
        _MIC_INDEX = int(_env_mic)
    except ValueError:
        print(f"[JARVIS] Warning: invalid JARVIS_MIC_INDEX={_env_mic!r}, using default")

_RECORD_SECONDS = int(os.getenv("JARVIS_RECORD_SECONDS", "8"))

_recognizer = sr.Recognizer()

# Vosk Offline STT Configuration
_project_root = Path(__file__).resolve().parent.parent
_DEFAULT_VOSK_PATH = _project_root / "vosk-model" / "vosk-model-small-en-us-0.15"
_VOSK_MODEL_PATH = os.getenv("JARVIS_VOSK_MODEL", str(_DEFAULT_VOSK_PATH))
_vosk_model = None


def _get_vosk_model():
    """Lazily load the Vosk model if needed."""
    global _vosk_model
    if _vosk_model is None:
        try:
            from vosk import Model
            if os.path.exists(_VOSK_MODEL_PATH):
                print(f"[JARVIS] Loading Vosk model from {_VOSK_MODEL_PATH}...")
                _vosk_model = Model(_VOSK_MODEL_PATH)
                print("[JARVIS] Vosk model loaded successfully.")
            else:
                print(f"[JARVIS] Warning: Vosk model not found at {_VOSK_MODEL_PATH}")
        except ImportError:
            print("[JARVIS] Warning: 'vosk' package is not installed. Offline STT will not work.")
    return _vosk_model


def listen() -> str | None:
    """
    Record audio from the microphone and return transcribed text.
    Returns None if nothing was heard or recognition failed.
    """
    # Wait until mic is enabled (e.g. music is not playing)
    while not mic_enabled():
        time.sleep(0.2)

    try:
        device = sd.query_devices(_MIC_INDEX, "input")
        sample_rate = int(device["default_samplerate"])

        print(f"[JARVIS] Listening on: {device['name']} @ {sample_rate}Hz")
        print("[JARVIS] Speak now...")

        audio = sd.rec(
            int(_RECORD_SECONDS * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
        )
        sd.wait()

        volume = np.abs(audio).mean()
        print(f"[JARVIS] Volume: {volume:.6f}")

        # Convert float32 [-1, 1] to int16
        audio_int16 = (audio * 32767).astype(np.int16)

        # Determine if we should use offline STT
        use_offline = os.getenv("JARVIS_STT_OFFLINE", "false").lower() in ("true", "1", "yes")

        if not use_offline:
            try:
                audio_data = sr.AudioData(
                    audio_int16.tobytes(),
                    sample_rate,
                    2,  # 2 bytes per sample (int16)
                )
                print("[JARVIS] Recognizing (Google Online)...")
                text = _recognizer.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                # Silence / nothing recognized
                return None
            except sr.RequestError as e:
                print(f"[JARVIS] Google STT error: {e}. Falling back to offline STT.")

        # Offline fallback / forced offline
        model = _get_vosk_model()
        if model:
            from vosk import KaldiRecognizer
            print("[JARVIS] Recognizing (Vosk Offline)...")
            rec = KaldiRecognizer(model, sample_rate)
            rec.AcceptWaveform(audio_int16.tobytes())
            result = json.loads(rec.FinalResult())
            text = result.get("text", "")
            return text if text.strip() else None
        else:
            print("[JARVIS] Offline STT fallback is unavailable (Vosk model missing or not installed).")
            return None

    except Exception as e:
        print(f"[JARVIS] Listen error: {e}")
        return None