import numpy as np
import matplotlib.pyplot as plt
import random


def crear_habitacion(mapa, min_size, max_size, tipo_habitacion):
    h = random.randint(min_size, max_size)
    w = random.randint(min_size, max_size)
    x = random.randint(1, mapa.shape[1] - w - 1)
    y = random.randint(1, mapa.shape[0] - h - 1)

    # Asegurar que la habitación no se superponga con otras
    if np.any(mapa[y : y + h, x : x + w] != ""):
        return False

    mapa[y : y + h, x : x + w] = tipo_habitacion
    return (x, y, w, h)


def crear_pasillo(mapa, desde, hasta, tipo_pasillo):
    x1, y1, w1, h1 = desde
    x2, y2, w2, h2 = hasta

    start_x = random.randint(x1, x1 + w1 - 1)
    start_y = random.randint(y1, y1 + h1 - 1)
    end_x = random.randint(x2, x2 + w2 - 1)
    end_y = random.randint(y2, y2 + h2 - 1)

    # Determinar dirección y dimensiones del pasillo
    if abs(start_x - end_x) > abs(start_y - end_y):  # Pasillo horizontal
        step = 1 if start_x < end_x else -1
        for x in range(start_x, end_x + step, step):
            mapa[start_y : max(start_y + 3, mapa.shape[0]), x] = tipo_pasillo
            if abs(x - start_x) > 7:
                break
    else:  # Pasillo vertical
        step = 1 if start_y < end_y else -1
        for y in range(start_y, end_y + step, step):
            mapa[y, start_x : max(start_x + 3, mapa.shape[1])] = tipo_pasillo
            if abs(y - start_y) > 7:
                break


def generar_mapa_dungeon(dimx, dimy):
    mapa = np.full((dimy, dimx), "", dtype=object)

    tipos_habitacion = ["dungeon", "boss", "god", "psycho", "hell"]
    tipos_pasillo = ["path"]

    habitaciones = []
    max_intentos = 100  # Evitar un bucle infinito si no hay más espacio
    intentos = 0
    while intentos < max_intentos:
        tipo_habitacion = random.choice(tipos_habitacion)
        nueva_habitacion = crear_habitacion(mapa, 4, 10, tipo_habitacion)
        if nueva_habitacion:
            if habitaciones:
                crear_pasillo(
                    mapa,
                    habitaciones[-1],
                    nueva_habitacion,
                    random.choice(tipos_pasillo),
                )
            habitaciones.append(nueva_habitacion)
        intentos += 1

    # Rellenar el resto del mapa con 'grass' y 'dirt'
    for y in range(mapa.shape[0]):
        for x in range(mapa.shape[1]):
            if mapa[y, x] == "":
                mapa[y, x] = random.choice(["grass", "dirt"])

    # Convertir nombres a colores RGB
    color_map = {
        "grass": [0, 128, 0],
        "dirt": [139, 69, 19],
        "path": [210, 180, 140],
        "dungeon": [128, 128, 128],
        "boss": [255, 0, 0],
        "god": [255, 255, 0],
        "psycho": [75, 0, 130],
        "hell": [0, 0, 0],
    }
    mapa_colorido = np.array([[color_map[cell] for cell in row] for row in mapa])

    # Visualización
    plt.figure(figsize=(10, 10))
    plt.imshow(mapa_colorido, interpolation="nearest")
    plt.title("Mapa de Mazmorra Procedural")
    plt.xticks([])
    plt.yticks([])
    plt.show()


# Ejemplo de uso
generar_mapa_dungeon(60, 60)
