import time
import numpy as np
import sounddevice as sd
import speech_recognition as sr
from tools.audio_mode import mic_enabled


MIC_INDEX = 12
RECORD_SECONDS = 5

r = sr.Recognizer()


def listen():

    while not mic_enabled():
        time.sleep(0.2)
    
    try:

        device = sd.query_devices(
            MIC_INDEX,
            "input"
        )

        sample_rate = int(
            device["default_samplerate"]
        )

        print(
            f"Listening... {sample_rate}"
        )

        print(
            "SPEAK NOW"
        )
        device = sd.query_devices(
        MIC_INDEX,    
        kind="input"
)

        sample_rate = int(
        device["default_samplerate"]
)

        print(
            device["name"]
        )

        print(device)

        audio = sd.rec(

            int(
                8 * sample_rate
            ),

            samplerate=sample_rate,

            channels=1,

            dtype="float32",


        )

        sd.wait()

        volume = np.abs(
            audio
        ).mean()

        print(
            "Volume:",
            volume
        )

        audio = (
            audio
            * 32767
        ).astype(
            np.int16
        )

        audio_data = sr.AudioData(

            audio.tobytes(),

            sample_rate,

            2

        )

        print(
            "Recognizing..."
        )

        text = (
            r.recognize_google(
                audio_data
            )
        )

        return text

    except Exception as e:

        print(
            e
        )

        return None