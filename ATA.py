# import des librairies

from traduction import traduction
from textToSpeech import textToSpeech
from speechToText import speechToText

print("Bonjour Bienvenu dans ATA, Assistant de Traduction Automatique")
print("Veillez prononcez la phrase à traduire en eng ")

texte = speechToText()
<<<<<<< HEAD
texte = traduction(texte)
textToSpeech(texte)
=======

print("J'ai entendu : " + texte)
texte, langue = traduction(texte)
textToSpeech(texte, langue)
>>>>>>> 2d2bd022454c6b8cc5d6924eaf5ce12d92917f35

print("J'ai fini !")
