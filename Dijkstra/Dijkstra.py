from queue import PriorityQueue
from collections import deque

class Graph:
    def __init__(self, n_nodos):
        self.n_nodos    = n_nodos
        self.enlaces    =   [[-1 for i in range(n_nodos)] 
                              for i in range(n_nodos)]
        self.visitados  = deque()

    def add_enlace(self, inicio, final, peso, both = False):
        self.enlaces[inicio][final]                     = peso
        if both == True:    self.enlaces[final][inicio] = peso


    def dijkstra(self, nodo_origen):
        distancias = {nodo:float('inf') for nodo in range(self.n_nodos)}
        distancias[nodo_origen] = 0

        pq = PriorityQueue()
        pq.put((0, nodo_origen))

        while not pq.empty():
            (dist , nodo_actual) = pq.get()
            self.visitados.append(nodo_actual)

            for vecino in range(self.n_nodos):
                if self.enlaces[nodo_actual][vecino] != -1:
                    costo_distancia = self.enlaces[nodo_actual][vecino]
                    if vecino not in self.visitados:
                        costo_actual = distancias[vecino]
                        costo_actualizado = distancias[nodo_actual] + costo_distancia

                        if costo_actual > costo_actualizado:
                            pq.put(( costo_actualizado, vecino))
                            distancias[vecino] = costo_actualizado
                            print(f'paso: {vecino} -> {costo_actual}:{costo_actualizado} ')
        return distancias

