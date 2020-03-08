# import des librairies

from traduction import traduction
from textToSpeech import textToSpeech
from speechToText import speechToText

print("Bonjour Bienvenu dans ATA, Assistant de Traduction Automatique")
print("Veillez prononcez la phrase à traduire en eng ")

texte = speechToText()

print("J'ai entendu : " + texte)
texte = traduction(texte)
textToSpeech(texte)

print("J'ai fini !")
