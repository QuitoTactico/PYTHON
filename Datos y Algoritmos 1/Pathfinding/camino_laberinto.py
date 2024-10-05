def camino(laberinto, origen, destino):
    return f(laberinto, origen[1], origen[0], destino, 0)


def f(l: list, x: int, y: int, d: list, c: int) -> int:
    if l[y][x] == 0:
        return 999999
    if x == d[1] and y == d[0]:
        print(str(c) + "-")
        return c

    l[y][x] = 0
    c = c + 1

    if x == 0 and y == 0:
        return min(f(l, x + 1, y, d, c), f(l, x, y + 1, d, c))
    if x == 0 and y == len(l) - 1:
        return min(f(l, x + 1, y, d, c), f(l, x, y - 1, d, c))
    if x == len(l[0]) - 1 and y == 0:
        return min(f(l, x - 1, y, d, c), f(l, x, y + 1, d, c))
    if x == len(l[0]) - 1 and y == len(l) - 1:
        return min(f(l, x - 1, y, d, c), f(l, x, y - 1, d, c))

    if x == 0:
        return min(f(l, x + 1, y, d, c), f(l, x, y - 1, d, c), f(l, x, y + 1, d, c))
    if x == len(l[0]) - 1:
        return min(f(l, x - 1, y, d, c), f(l, x, y - 1, d, c), f(l, x, y + 1, d, c))
    if y == 0:
        return min(f(l, x - 1, y, d, c), f(l, x + 1, y, d, c), f(l, x, y + 1, d, c))
    if y == len(l) - 1:
        return min(f(l, x - 1, y, d, c), f(l, x + 1, y, d, c), f(l, x, y - 1, d, c))

    return min(
        f(l, x - 1, y, d, c),
        f(l, x + 1, y, d, c),
        f(l, x, y - 1, d, c),
        f(l, x, y + 1, d, c),
    )


# print(return min(1,3,8,1,4,25,23,5,2,34,5,2,-124))
#        0  1  2  3  4  5  6  7  8  9
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
# print(len(lab[0]))
i = [0, 0]
d = [7, 5]
dd = [0, 2]
print(camino(l, i, d))
# print(lab[4][6])
# print(len(l[1]))
