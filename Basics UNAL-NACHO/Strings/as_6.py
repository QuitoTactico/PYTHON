with open("mensaje.txt", "r") as fichero:
    for linea in fichero:
        print(linea.replace("\n", "")[::-1])
