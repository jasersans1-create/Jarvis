import pvporcupine
import sounddevice as sd
import struct

def wait_for_wake_word():
    porcupine = pvporcupine.create(keywords=["jarvis"])

    stream = sd.RawInputStream(
        samplerate=porcupine.sample_rate,
        blocksize=porcupine.frame_length,
        dtype="int16",
        channels=1,
    )

    stream.start()

    print("🔵 Waiting for wake word: JARVIS")

    while True:
        pcm, _ = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)

        if result >= 0:
            print("🟢 Wake word detected!")
            return True