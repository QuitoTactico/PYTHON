from datos import generarDatos

if __name__ == "__main__":
    muestra = generarDatos(1000)

    for elemento in muestra:
        print(elemento)
