# import des librairies
from gtts import gTTS
import os
from langdetect import detect
from playsound import playsound

def textToSpeech(texte):
    langue = detect(texte)
    tts = gTTS(text=texte, lang=langue)
    tts.save("good.mp3")
    playsound("good.mp3")
