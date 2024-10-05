import heapq


def path_finder(maze):
    maze = [list(map(int, row)) for row in maze.split()]
    N = len(maze)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dijkstra():
        pq = [(0, 0, 0)]  # (cost, x, y)
        visited = [[False] * N for _ in range(N)]
        costs = [[float("inf")] * N for _ in range(N)]
        costs[0][0] = 0

        while pq:
            cost, x, y = heapq.heappop(pq)
            if visited[x][y]:
                continue
            visited[x][y] = True

            if x == N - 1 and y == N - 1:
                return cost

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    new_cost = cost + abs(maze[nx][ny] - maze[x][y])
                    if new_cost < costs[nx][ny]:
                        costs[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))

        return float("inf")

    return dijkstra()


b = "\n".join(["010", "010", "010"])

a = "\n".join(["7000", "0777", "0777", "0777", "0777", "0000"])

e = "\n".join(["700000", "077770", "077770", "077770", "077770", "000007"])

f = "\n".join(["777000", "007000", "007000", "007000", "007000", "007777"])

g = "\n".join(["000000", "000000", "000000", "000010", "000109", "001010"])

h = "99321659285\n82274152378\n95311209346\n11818079185\n50926731149\n06934617619\n05718311124\n91803296898\n42959100694\n70004528365\n76632198148"

print(path_finder(h))
