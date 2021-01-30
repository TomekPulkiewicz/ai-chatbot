import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from pydub import AudioSegment
import time
fs = 44100
duration = 5  # seconds
r = sr.Recognizer()


def recordAudio():

    myrecording = sd.rec(duration * fs, samplerate=fs,
                         channels=2, dtype='float64')
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete , Play Audio")
    sd.play(myrecording, fs)
    sd.save
    sd.wait()
    print("Play Audio Complete")


def recogniceAudio():
    recordAudio()
    file = sr.AudioFile("output.flac")
    with file as source:
        audio = r.record(source)
        print
        return r.recognize_google(audio)


print(recogniceAudio())
