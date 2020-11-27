# pySpeech.py
# Python wrapper around SAPI5.
#
# Copyright 2020 Ty Gillespie. All rights reserved
# MIT Licensed.

import win32com.client

import os


synth = None


class SynthConstants:
    """Speaking flags, such as async."""

    SVS_FLAGS_ASYNC = 1
    SVSF_PURGE_BEFORE_SPEAK = 2


def initialize():
    """Initializes the speech system."""
    global synth
    if synth is not None:
        return False
    synth = win32com.client.Dispatch("sapi.SPVoice")
    return True


def getRate():
    """Returns the rate of the synth object."""
    global synth
    if synth is None:
        return False
    return (synth.Rate + 10) * 5


def getVolume():
    """Returns the volume of the synth object."""
    global synth
    if synth is None:
        return False
    return synth.Volume


def getVoice():
    """Returns the current SAPI voice."""
    global synth
    if synth is None:
        return False
    return os.path.basename(synth.Voice.Id)


def setRate(value):
    """Sets the speech rate of the synth object."""
    global synth
    if synth is None:
        return False
    synth.Rate = (value / 5) - 10
    return True


def setVolume(value):
    """Sets the volume of the synth object"""
    global synth
    if synth is None:
        return False
    synth.Volume = value
    return True


def speak(text, wait=False):
    """Speaks a string of text."""
    global synth
    if synth is None:
        return False
    flags = 0
    if wait is False:
        flags = SynthConstants.SVS_FLAGS_ASYNC
    synth.Speak(text, flags)


def cancel():
    """Stops the speech."""
    global synth
    if synth is None:
        return False
    if synth.Status.RunningState == 2:
        synth.Speak(
            "", SynthConstants.SVS_FLAGS_ASYNC | SynthConstants.SVSF_PURGE_BEFORE_SPEAK
        )
