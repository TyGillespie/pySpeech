# test.py
# pySpeech test script.
#
# Copyright 2020 Ty Gillespie. All rights reserved.
# MIT Licensed.

import pySpeech

import sys


if __name__ == "__main__":
    pySpeech.initialize()

    # Async
    pySpeech.speak("This is a test.")
    input()
    pySpeech.cancel()

    # Non-async
    pySpeech.speak("Another test", True)
    input()

    sys.exit()
