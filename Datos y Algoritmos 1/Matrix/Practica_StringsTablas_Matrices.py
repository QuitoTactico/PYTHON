m1, m2, dim1, dim2 = {}, {}, input().split("x"), input().split("x")
if int(dim1[1]) != int(dim2[0]):
    print(
        "Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla"
    )
    quit()
for i in range(int(dim1[0])):
    m1[i] = {}
    for j in range(int(dim1[1])):
        m1[i][j] = int(input())
for i in range(int(dim2[0])):
    m2[i] = {}
    for j in range(int(dim2[1])):
        m2[i][j] = int(input())
for i in range(int(dim1[0])):
    s = ""
    for j in range(int(dim2[1])):
        c = 0
        for y in range(int(dim1[1])):
            for x in range(int(dim1[1])):
                if x == y:
                    c += m1[i][x] * m2[y][j]
        s += str(c) + " "
    print(s[:-1])
