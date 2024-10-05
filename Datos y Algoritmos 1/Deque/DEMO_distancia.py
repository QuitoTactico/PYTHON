from collections import deque

numeros = deque(map(int, input().split()))
thash = {}
for i in range(len(numeros)):
    thash[numeros[i]] = {"primera_aparicion": "-", "distancia": 0}
for i in range(
    len(numeros)
):  # AGREGA APARICION INICIAL, Y SU DISTANCIA CON LA APARICION ACTUAL
    if thash[numeros[i]]["primera_aparicion"] == "-":
        thash[numeros[i]]["primera_aparicion"] = i
    else:
        thash[numeros[i]].update(
            {"distancia": i - thash[numeros[i]]["primera_aparicion"]}
        )
distancias = deque()
for i in deque(thash.keys()):
    distancias.append(thash[i]["distancia"])
print(max(distancias))  # IMPRIME LA MAYOR DE ELLAS
