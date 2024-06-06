import heapq

# Crear una lista
lista = [5, 7, 9, 1, 3]

# Convertir la lista en un montículo mínimo
heapq.heapify(lista)
print("Montículo después de heapify:", lista)

# Insertar un nuevo elemento
heapq.heappush(lista, 4)
print("Montículo después de heappush(4):", lista)

# Eliminar y retornar el elemento mínimo
min_element = heapq.heappop(lista)
print("Elemento mínimo eliminado:", min_element)
print("Montículo después de heappop():", lista)
