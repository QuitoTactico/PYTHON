# pip install SpeechRecognition
# pip install sounddevice
# pip install soundfile

import speech_recognition as s_recogition
import sounddevice as s_device
import soundfile as s_file


def listen_and_write():
    # ---------------Grabación de voz------------------

    # Configurar la duración de la grabación y la frecuencia de muestreo
    duration = 10  # segundos
    fs = 44100  # frecuencia de muestreo

    print("TALK NOW")
    # Grabar audio con sounddevice
    myrecording = s_device.rec(
        int(duration * fs), samplerate=fs, channels=2, dtype="float64"
    )
    s_device.wait()

    # Guardar la grabación en un archivo WAV
    s_file.write("output.wav", myrecording, fs)

    # ---------------Reconocimiento de voz------------------
    # Utilizar el archivo WAV como fuente de audio
    with s_recogition.AudioFile("output.wav") as source:
        # Crear un objeto de reconocimiento de voz
        reconocedor = s_recogition.Recognizer()

        audio = reconocedor.record(source)

        try:
            # Convertir el audio en texto
            text = reconocedor.recognize_google(audio, language="es")

            # Escribir el texto en un archivo de texto
            with open("texto.txt", "w", encoding="UTF-8") as file:
                file.write(text + "\n")

        except:
            print("No se pudo reconocer el audio")


if __name__ == "__main__":
    listen_and_write()


"""
Por ahora guardamos el audio en un archivo WAV y luego lo leemos para convertirlo en texto.
¿Se puede hacer todo en un solo paso? (leerlo con soundrecognition des_devicee el objeto de sounddevice sin tener que guardarlo con soundfile).

Podríamos hacer que cuando no se reconozca el audio, se vuelva a grabar, pero no sabemos como hacer que se sobreescriba el archivo WAV, y no se guarde como output1.wav, output2.wav, etc. Tendríamos que borrar el archivo y volverlo a crear.

También podríamos hacer que se grabe indefinidamente hasta que haya un silencio de 2 segundos, pero tendríamos que investigar en la documentacion de sounddevice para ver si existe función de autocortado o de duración dinámica.

La otras librería que quisimos probar fué scipy.io.wavfile (scipy) pero no funcionó, guardaba el audio de una forma que no podía leer SpeechRecognition aunque fuera formato .wav

La libreía speech_recognition (s_recogition) tenía una función llamada microphone() que permitía grabar audio directamente des_devicee el micrófono, pero usaba la librería PyAudio que a su vez usaba distutils. Una librería que venía por default en python, pero quedó obsoleta des_devicee python 3.10 así que tuvimos que cambiar todo estando ya muy cerca.

Soundfile, puede guardar el audio en formato .flac si quereremos, no sé si sea de mejor calidad o si es más compacto, o menos propenso a corromperse. 
"""
