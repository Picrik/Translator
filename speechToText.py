import speech_recognition as sr

def speechToText():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("ATA à entendu " + r.recognize_google(audio, language = "fr-FR"))
        texte = r.recognize_google(audio, language = "fr-FR")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    if texte:
        return texte
