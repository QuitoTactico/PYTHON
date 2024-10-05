# pip install SpeechRecognition
# pip install sounddevice
# pip install numpy
# pip install scipy

import speech_recognition as sr
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write


def listen():
    # Crear un objeto de reconocimiento de voz
    r = sr.Recognizer()

    # Configurar la duración de la grabación y la frecuencia de muestreo
    duration = 10  # segundos
    fs = 44100  # frecuencia de muestreo

    # Grabar audio con sounddevice
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    # Guardar la grabación en un archivo WAV
    write("output.wav", fs, myrecording)


"""
    # Utilizar el archivo WAV como fuente de audio
    with sr.AudioFile('output.wav') as source:
        audio = r.record(source)
        try:
            # Convertir el audio en texto
            text = r.recognize_google(audio, language="es")

            # Escribir el texto en un archivo de texto
            with open("texto.txt", "a") as file:
                file.write(text + "\n")
        except Exception as e:
            print("Error: ", str(e))
"""


def my_write():
    # Crear un objeto de reconocimiento de voz
    r = sr.Recognizer()

    # Abrir el archivo de audio
    with sr.AudioFile("output.wav") as source:
        # Escuchar el archivo de audio
        audio_data = r.record(source)
        # Convertir el audio a texto
        text = r.recognize_google(audio_data, language="es-ES")
        print(text)


if __name__ == "__main__":
    listen()
    my_write()
