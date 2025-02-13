import numpy as np
import matplotlib.pyplot as plt
import random


class Habitacion:
    def __init__(self, x, y, w, h, tipo):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tipo = tipo
        self.conectado = False


def crear_habitacion(mapa, min_size, max_size, tipo_habitacion):
    h = random.randint(min_size, max_size)
    w = random.randint(min_size, max_size)
    x = random.randint(1, mapa.shape[1] - w - 1)
    y = random.randint(1, mapa.shape[0] - h - 1)

    # Asegurar que la habitación no se superponga con otras
    if np.any(mapa[y : y + h, x : x + w] != ""):
        return None

    return Habitacion(x, y, w, h, tipo_habitacion)


def conectar_habitaciones(mapa, habitacion1, habitacion2, tipo_pasillo):
    puntos1 = (
        random.randint(habitacion1.x, habitacion1.x + habitacion1.w - 1),
        random.randint(habitacion1.y, habitacion1.y + habitacion1.h - 1),
    )
    puntos2 = (
        random.randint(habitacion2.x, habitacion2.x + habitacion2.w - 1),
        random.randint(habitacion2.y, habitacion2.y + habitacion2.h - 1),
    )

    # Crear un pasillo horizontal o vertical
    if random.random() < 0.5:  # horizontal primero, luego vertical
        for x in range(min(puntos1[0], puntos2[0]), max(puntos1[0], puntos2[0]) + 1):
            mapa[puntos1[1], x] = tipo_pasillo
        for y in range(min(puntos1[1], puntos2[1]), max(puntos1[1], puntos2[1]) + 1):
            mapa[y, puntos2[0]] = tipo_pasillo
    else:  # vertical primero, luego horizontal
        for y in range(min(puntos1[1], puntos2[1]), max(puntos1[1], puntos2[1]) + 1):
            mapa[y, puntos1[0]] = tipo_pasillo
        for x in range(min(puntos1[0], puntos2[0]), max(puntos1[0], puntos2[0]) + 1):
            mapa[puntos2[1], x] = tipo_pasillo


def generar_mapa_dungeon(dimx, dimy):
    mapa = np.full((dimy, dimx), "", dtype=object)

    tipos_habitacion = ["dungeon", "boss", "god", "psycho", "hell", "grass", "dirt"]
    tipos_pasillo = ["path", "dungeon"]

    habitaciones = []
    while len(habitaciones) < 100:
        tipo_habitacion = random.choice(tipos_habitacion)
        nueva_habitacion = crear_habitacion(mapa, 4, 10, tipo_habitacion)
        if nueva_habitacion:
            if habitaciones:
                conectar_habitaciones(
                    mapa,
                    habitaciones[-1],
                    nueva_habitacion,
                    random.choice(tipos_pasillo),
                )
            habitaciones.append(nueva_habitacion)

    # Rellenar las habitaciones y los pasillos en el mapa
    for habitacion in habitaciones:
        mapa[
            habitacion.y : habitacion.y + habitacion.h,
            habitacion.x : habitacion.x + habitacion.w,
        ] = habitacion.tipo

    # Convertir nombres a colores RGB
    color_map = {
        "": [0, 0, 0],
        "path": [210, 180, 140],
        "dungeon": [128, 128, 128],
        "boss": [255, 0, 0],
        "god": [255, 255, 0],
        "psycho": [75, 0, 130],
        "hell": [0, 0, 0],
        "grass": [0, 128, 0],
        "dirt": [139, 69, 19],
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
generar_mapa_dungeon(300, 60)
