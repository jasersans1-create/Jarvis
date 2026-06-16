MIC_ENABLED = True


def disable_mic():

    global MIC_ENABLED

    MIC_ENABLED = False

    print("[JARVIS] Mic disabled")


def enable_mic():

    global MIC_ENABLED

    MIC_ENABLED = True

    print("[JARVIS] Mic enabled")


def mic_enabled():

    return MIC_ENABLED