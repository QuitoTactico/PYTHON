# pip install SpeechRecognition
# pip install PyAudio

import speech_recognition as sr
import os

def listen_and_write():
    # Crear un objeto de reconocimiento de voz
    r = sr.Recognizer()

    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
        # Convertir el audio en texto
        text = r.recognize_google(audio, language="es")

        # Escribir el texto en un archivo de texto
        with open("texto.txt", "a") as file:
            file.write(text + "\n")

        print("Texto escrito en el archivo 'texto.txt'")
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error al solicitar el servicio de reconocimiento de voz; {0}".format(e))

# Será llamarla desde afuera para testearla más rápido
listen_and_write()
