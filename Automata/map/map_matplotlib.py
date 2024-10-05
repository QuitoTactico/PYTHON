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
        self.tesoro = False
        self.boss = False
        self.spawn = False
        self.portal = False


def crear_habitacion(mapa, min_size, max_size, tipo_habitacion):
    h = random.randint(min_size, max_size)
    w = random.randint(min_size, max_size)
    x = random.randint(1, mapa.shape[1] - w - 1)
    y = random.randint(1, mapa.shape[0] - h - 1)

    # Asegurar que la habitación no se superponga con otras
    if np.any(mapa[y : y + h, x : x + w] != ""):
        return None

    return Habitacion(x, y, w, h, tipo_habitacion)


def designar_habitaciones_especiales(habitaciones):
    # Seleccionar habitación para spawn de jugadores
    habitacion_spawn = random.choice(habitaciones)
    habitacion_spawn.spawn = True

    # Seleccionar tres habitaciones para jefes
    habitaciones_boss = 0
    while habitaciones_boss < 3:
        h = random.choice(habitaciones)
        if not h.spawn:
            h.boss = True
            habitaciones_boss += 1

    # Seleccionar habitaciones para tesoros
    for h in habitaciones:
        if random.random() < 0.15:  # 15% de probabilidad de tener tesoro
            h.tesoro = True

    # Seleccionar habitaciones para portales
    habitaciones_portal = 0
    while habitaciones_portal < int(
        len(habitaciones) * 0.015
    ):  # el 2% de las habitaciones tienen portal
        h = random.choice(habitaciones)
        if not h.spawn and not h.boss:
            h.portal = True
            habitaciones_portal += 1


def distancia(h1, h2):
    # Calcular la distancia entre el centro de dos habitaciones
    centro_h1 = (h1.x + h1.w // 2, h1.y + h1.h // 2)
    centro_h2 = (h2.x + h2.w // 2, h2.y + h2.h // 2)
    return np.sqrt(
        (centro_h1[0] - centro_h2[0]) ** 2 + (centro_h1[1] - centro_h2[1]) ** 2
    )


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
    ancho_pasillo = random.randint(1, 2)
    if random.random() < 0.5:  # horizontal primero, luego vertical
        for x in range(min(puntos1[0], puntos2[0]), max(puntos1[0], puntos2[0]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos1[1] + offset < mapa.shape[0]:
                    mapa[puntos1[1] + offset, x] = tipo_pasillo
        for y in range(min(puntos1[1], puntos2[1]), max(puntos1[1], puntos2[1]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos2[0] + offset < mapa.shape[1]:
                    mapa[y, puntos2[0] + offset] = tipo_pasillo
    else:  # vertical primero, luego horizontal
        for y in range(min(puntos1[1], puntos2[1]), max(puntos1[1], puntos2[1]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos1[0] + offset < mapa.shape[1]:
                    mapa[y, puntos1[0] + offset] = tipo_pasillo
        for x in range(min(puntos1[0], puntos2[0]), max(puntos1[0], puntos2[0]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos2[1] + offset < mapa.shape[0]:
                    mapa[puntos2[1] + offset, x] = tipo_pasillo


def generar_mapa_dungeon(dimx, dimy):
    mapa = np.full((dimy, dimx), "", dtype=object)

    total_tiles = dimx * dimy  # 200
    num_habitaciones = total_tiles // 200  # 1 habitación por cada 200 tiles

    tipos_habitacion = ["psycho", "hell", "grass", "dirt"]
    tipos_pasillo = ["path", "dungeon"]

    habitaciones = []
    while len(habitaciones) < num_habitaciones:
        tipo_habitacion = random.choice(tipos_habitacion)
        nueva_habitacion = crear_habitacion(mapa, 4, 10, tipo_habitacion)
        if nueva_habitacion:
            if habitaciones:
                # Conectar con la habitación más cercana
                habitacion_cercana = min(
                    habitaciones, key=lambda h: distancia(h, nueva_habitacion)
                )
                conectar_habitaciones(
                    mapa,
                    habitacion_cercana,
                    nueva_habitacion,
                    random.choice(tipos_pasillo),
                )
            habitaciones.append(nueva_habitacion)

    # Designar habitaciones para spawn de jugadores, jefes y tesoros
    designar_habitaciones_especiales(habitaciones)

    # Rellenar las habitaciones y los pasillos en el mapa
    for habitacion in habitaciones:
        if habitacion.spawn:
            mapa[
                habitacion.y : habitacion.y + habitacion.h,
                habitacion.x : habitacion.x + habitacion.w,
            ] = "spawn"
        elif habitacion.boss:
            mapa[
                habitacion.y : habitacion.y + habitacion.h,
                habitacion.x : habitacion.x + habitacion.w,
            ] = "boss"
        elif habitacion.tesoro:
            mapa[
                habitacion.y : habitacion.y + habitacion.h,
                habitacion.x : habitacion.x + habitacion.w,
            ] = "treasure"
        elif habitacion.portal:
            mapa[
                habitacion.y : habitacion.y + habitacion.h,
                habitacion.x : habitacion.x + habitacion.w,
            ] = "portal"
        else:
            mapa[
                habitacion.y : habitacion.y + habitacion.h,
                habitacion.x : habitacion.x + habitacion.w,
            ] = habitacion.tipo

    # Convertir nombres a colores RGB
    """
    color_map = {'': [0, 0, 0], 'path': [210, 180, 140], 'dungeon': [128, 128, 128], 'boss': [255, 0, 0], 'god': [255, 255, 0], 'psycho': [75, 0, 130], 'hell': [11, 111, 11], 'grass': [0, 128, 0], 'dirt': [139, 69, 19], 'Spawn': [255, 255, 224], 'Boss': [255, 0, 0], 'Treasure': [255, 223, 0]}
    """
    color_map = {
        "": [0, 0, 0],
        "path": [210, 180, 140],
        "dungeon": [128, 128, 128],
        "god": [255, 255, 255],
        "psycho": [255, 255, 255],
        "hell": [255, 255, 255],
        "grass": [255, 255, 255],
        "dirt": [255, 255, 255],
        "spawn": [0, 0, 255],
        "boss": [255, 0, 0],
        "treasure": [0, 255, 0],
        "portal": [255, 100, 255],
    }

    mapa_colorido = np.array([[color_map[cell] for cell in row] for row in mapa])

    # Visualización
    plt.figure(figsize=(10, 10))
    plt.imshow(mapa_colorido, interpolation="nearest")
    plt.title("Mapa de Mazmorra Procedural con Juego Integrado")
    plt.xticks([])
    plt.yticks([])
    plt.show()


# Ejemplo de uso
# no más de 500.000 tiles
generar_mapa_dungeon(700, 700)
