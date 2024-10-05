def camino(laberinto, origen, destino):
    destino[0] = destino[0] + 1
    destino[1] = destino[1] + 1
    sol = f(laberinto, origen[0] + 1, origen[1] + 1, destino, 0)
    if sol == 999999:
        return -1
    return sol


def f(l: list, y: int, x: int, d: list, c: int) -> int:
    if l[y][x] == 0:
        return 999999
    if x == d[1] and y == d[0]:
        return c
    l[y][x] = 0
    return min(
        f(l, y + 1, x, d, c + 1),
        f(l, y, x + 1, d, c + 1),
        f(l, y - 1, x, d, c + 1),
        f(l, y, x - 1, d, c + 1),
    )

    # 0  1  2  3  4  5  6  7  8  9


l = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],  # 0
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],  # 1
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],  # 2
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],  # 3
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # 4
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],  # 5
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],  # 6
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # 7
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],  # 8
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
]  # 9

ll = [[1, 1, 1], [0, 1, 1], [0, 1, 1]]


zero = [0] * len(l)
l.insert(0, zero)
l.append(zero)
for i in range(len(l)):
    l[i].insert(0, 0)
    l[i].append(0)
print(l)

print(camino(l, [0, 0], [7, 5]))  # importante#
