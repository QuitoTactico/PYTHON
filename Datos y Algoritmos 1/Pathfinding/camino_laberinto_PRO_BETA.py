def camino(laberinto, origen, destino):
    destino[0] = destino[0] + 1
    destino[1] = destino[1] + 1
    # origen[0]= origen[0]+1
    # origen[1]= origen[1]+1
    # return f(laberinto,origen[1],origen[0],destino,0)
    return f(laberinto, 1, 1, 8, 6, 0)


def f(l: list, y: int, x: int, finy: int, finx: int, c: int) -> int:
    if l[y][x] == 0:
        return 999999
    if x == finx and y == finy:
        print(str(c) + "-")
        return c
    c = c + 1
    l[y][x] = 0
    return min(
        f(l, y + 1, x, finy, finx, c),
        min(
            f(l, y, x + 1, finy, finx, c),
            min(f(l, y - 1, x, finy, finx, c), f(l, y, x - 1, finy, finx, c)),
        ),
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
# print(camino(l,i,d))  #importante#
zero = [0] * len(l)
l.insert(0, zero)
l.append(zero)
for i in range(len(l)):
    l[i].insert(0, 0)
    l[i].append(0)
print(l)
# print(zero)
print(camino(l, i, d))  # importante#
