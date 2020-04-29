# import des librairies
from gtts import gTTS
import os
from playsound import playsound

def textToSpeech(texte, langue):
    tts = gTTS(text=texte, lang=langue)
    tts.save("good.mp3")
    playsound("good.mp3", True)
    os.remove("good.mp3")
