# man, idk no sé de dict (es hash)


"""P I E N S A"""


"""# recorre list map spl
# a cada uno le crea un key

ingresar la primera posición en la que existió, en la primera pos (cada value es una list)

# los que están repetidos no crean más key (verificar si existe)
si existe, poner su segunda aparición en la list[1] (segunda pos), y su resta con primera pos, en tercera pos
si sigue apareciendo, sobreescribir esa segunda pos, y actualizar la resta (pos 2 y 3 respectivamente)

format. = [first_ap , second/actual_ap, distance_between(dependiente, es [1]-[0])]
defaults = [0,"-","0"]   (le puedo poner None a [1]??)

recorrer diccionario con contador de max, y retornar ese max
o imprimirlo, qué importa, ya está hecho
coronao papi


"""

from collections import deque

# basura = input()  ###
numeros = deque(map(int, input().split()))

# print(list(numeros))   ###

thash = {}

for i in range(len(numeros)):  # LO VUELVE TODO UN DICCIONARIO
    thash[numeros[i]] = {"primera_aparicion": "-", "distancia": 0}


for i in range(len(numeros)):  # LO VUELVE TODO UN DICCIONARIO
    if thash[numeros[i]]["primera_aparicion"] == "-":
        thash[numeros[i]]["primera_aparicion"] = i
    else:
        thash[numeros[i]].update(
            {"distancia": i - thash[numeros[i]]["primera_aparicion"]}
        )

# for i in range(len(numeros)):


# print(thash[2]["primera_aparicion"])   ###
# print(thash[2]["distancia"])           ###

distancias = deque()

for i in deque(thash.keys()):
    distancias.append(thash[i]["distancia"])

# print(distancias)  ###

print(max(distancias))
