"""
detector.py — Wake word detection using openwakeword.

This module provides an alternative wake word detector using the
openwakeword library, which is fully open source and free.

NOTE: This module is NOT used by default. The main loop in main.py
uses text-based wake word detection (brain/wake.py) which requires
no extra dependencies. Use this module if you want hardware-level
wake word detection.

To use openwakeword:
  pip install openwakeword
  python -c "import openwakeword; openwakeword.utils.download_models()"

Environment variables:
  JARVIS_WAKE_THRESHOLD — confidence threshold for detection (default: 0.5)
"""

import os

try:
    import sounddevice as sd
    import numpy as np
    from openwakeword.model import Model

    _THRESHOLD = float(os.getenv("JARVIS_WAKE_THRESHOLD", "0.5"))

    def wait_for_wake_word() -> bool:
        """
        Listen continuously for the wake word using openwakeword.
        Returns True when detected.
        """
        model = Model(wakeword_models=["hey_jarvis"])
        sample_rate = 16000
        chunk_size = 1280  # 80ms at 16kHz

        print("[JARVIS] Waiting for wake word...")

        with sd.InputStream(samplerate=sample_rate, channels=1, dtype="int16", blocksize=chunk_size) as stream:
            while True:
                audio_chunk, _ = stream.read(chunk_size)
                audio_flat = audio_chunk.flatten()
                prediction = model.predict(audio_flat)

                for wakeword, score in prediction.items():
                    if score >= _THRESHOLD:
                        print(f"[JARVIS] Wake word detected! ({wakeword}: {score:.2f})")
                        return True

except ImportError:
    def wait_for_wake_word() -> bool:
        """Fallback: openwakeword not installed."""
        raise ImportError(
            "openwakeword is not installed. Install it with:\n"
            "  pip install openwakeword\n"
            "Or use the built-in text-based wake word detection in brain/wake.py"
        )