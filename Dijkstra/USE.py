from Dijkstra import *

grafo = Graph(9)

with open('grafo.txt', 'r') as fichero:
    for linea in fichero:
        origen, destino, peso = map(int, linea.split())
        grafo.add_enlace( origen , destino , peso, both = True )

nodo_inicio = 0
Distancias = grafo.dijkstra(nodo_inicio)
print(f'Resultado Dijkstra: {Distancias}')

for nodo in range(len(Distancias)):
    pass

for a in Distancias:
    print(a)