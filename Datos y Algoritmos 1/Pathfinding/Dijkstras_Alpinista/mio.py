import heapq


def path_finder(maze):
    # Convertir el input en una lista de listas de enteros
    maze = [list(map(int, row)) for row in maze.split()]
    N = len(maze)
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]  # Movimientos posibles: Este, Sur, Oeste, Norte

    def dijkstra():
        pq = [(0, 0, 0)]  # Cola de prioridad inicial con (costo, x, y)
        visited = [[False] * N for _ in range(N)]  # Matriz de nodos visitados
        costs = [
            [float("inf")] * N for _ in range(N)
        ]  # Matriz de costos inicializada con infinito
        costs[0][0] = 0  # Costo inicial en el punto de partida es 0

        while pq:
            cost, x, y = heapq.heappop(pq)  # Extraer el nodo con el menor costo
            if visited[x][y]:  # Si ya fue visitado, continuar con el siguiente
                continue
            visited[x][y] = True  # Marcar el nodo como visitado

            if x == N - 1 and y == N - 1:  # Si llegamos al destino, retornar el costo
                return cost

            # Explorar los nodos adyacentes
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < N and 0 <= ny < N and not visited[nx][ny]
                ):  # Asegurarse de que el nodo es válido y no visitado
                    new_cost = cost + abs(
                        maze[nx][ny] - maze[x][y]
                    )  # Calcular el nuevo costo, varía según ejercicio
                    if (
                        new_cost < costs[nx][ny]
                    ):  # Si el nuevo costo es menor, actualizarlo
                        costs[nx][ny] = new_cost
                        heapq.heappush(
                            pq, (new_cost, nx, ny)
                        )  # Añadir el nodo a la cola de prioridad

        return float("inf")  # Retornar infinito si no se puede llegar al destino

    return dijkstra()


b = "\n".join(["010", "010", "010"])

a = "\n".join(["7000", "0777", "0777", "0777", "0777", "0000"])

e = "\n".join(["700000", "077770", "077770", "077770", "077770", "000007"])

f = "\n".join(["777000", "007000", "007000", "007000", "007000", "007777"])

g = "\n".join(["000000", "000000", "000000", "000010", "000109", "001010"])

h = "99321659285\n82274152378\n95311209346\n11818079185\n50926731149\n06934617619\n05718311124\n91803296898\n42959100694\n70004528365\n76632198148"

print(path_finder(h))
