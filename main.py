from model.predict import predict
import pyttsx3
import os
import spotify
engine = pyttsx3.init()

en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.setProperty('volume', 2)
spotify.login()


def say(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


os.system("cls")
while True:
    msg = input(":")
    if msg == "quit":
        spotify.quit()
        break

    say(predict(msg))
