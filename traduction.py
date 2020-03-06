# import des librairies
from translate import Translator
from langdetect import detect

def traduction(texte):
    langue = detect(texte)
    translator = Translator(to_lang="en", from_lang="fr")
    translation = translator.translate(texte)

    return translation
