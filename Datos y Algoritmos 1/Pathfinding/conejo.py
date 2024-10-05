def f(M: list, x: int, y: int, k: int, d: int, cont: int) -> int:
    if M[y][x] == "#":
        cont = cont + k
    if M[y][x] == "*":
        cont = cont + d
    if (x == len(M[0]) - 1) and (y == len(M) - 1):
        return cont
    if x == len(M[0]) - 1:
        return f(M, x, y + 1, k, d, cont)
    if y == len(M) - 1:
        return f(M, x + 1, y, k, d, cont)
    return max(f(M, x, y + 1, k, d, cont), f(M, x + 1, y, k, d, cont))


X, Y = map(int, input().split())
k, d = map(int, input().split())
M = [[".", "#", "."], [".", "*", "*"], [".", ".", "#"]]

NN = [[]]
NN[0] = list(map(str, input().split()))


def g(NN: list, Y: int, c: int) -> list:
    if Y < (c + 2):
        return NN
    N = [[]]
    N[0] = list(map(str, input().split()))
    NN.extend(N)
    return g(NN, Y, c + 1)


# print(g(NN,Y,0))

# print(M[0][1])
# print(max(5,2))
temp = 0
if d > k:
    temp = d
    d = k
    k = temp

print(f(g(NN, Y, 0), 0, 0, k, d, 0))
