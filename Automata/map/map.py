import numpy as np
import matplotlib.pyplot as plt
import random


def crear_habitacion(mapa, min_size, max_size, tipo_habitacion):
    h = random.randint(min_size, max_size)
    w = random.randint(min_size, max_size)
    x = random.randint(1, mapa.shape[1] - w - 1)
    y = random.randint(1, mapa.shape[0] - h - 1)

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

    for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
        mapa[start_y, x] = tipo_pasillo

    for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
        mapa[y, end_x] = tipo_pasillo


def generar_mapa_dungeon(dimx, dimy, n_habitaciones=10):
    mapa = np.full((dimy, dimx), "", dtype=object)

    tipos_habitacion = ["dungeon", "boss", "god", "psycho", "hell"]
    tipos_pasillo = ["path"]

    habitaciones = []
    for _ in range(n_habitaciones):
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
generar_mapa_dungeon(300, 40, 20)
