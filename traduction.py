# import des librairies
from translate import Translator

def traduction(texte):
    translator = Translator(to_lang="en", from_lang="fr")
    translation = translator.translate(texte)

    return translation, "en"
