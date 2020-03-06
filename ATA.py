# import des librairies

from traduction import traduction
from textToSpeech import textToSpeech

print("Bonjour Bienvenu dans ATA, Assistant de Traduction Automatique")
texte = input("Veillez entrez la phrase à traduire en eng ")

texte = traduction(texte)
textToSpeech(texte)

print("J'ai fini !")
