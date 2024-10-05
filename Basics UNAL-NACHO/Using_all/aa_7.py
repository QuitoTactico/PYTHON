signo = {"+": True, "-": False}  # MI FAVORITO DE ESTE


def generar(n: int) -> list:
    m = []
    for _ in range(n):
        m.append(list(range(1, n + 1)))
    return m


def movx(m: list, n: int, d: bool) -> list:
    m[n - 1] = [m[n - 1][-1]] + m[n - 1][:-1] if d else m[n - 1][1:] + [m[n - 1][0]]
    return m


def movy(m: list, n: int, d: bool) -> list:
    temp, rng, it, bl = (
        m[-1][n - 1] if d else m[0][n - 1],
        range(len(m) - 1, -1, -1) if d else range(len(m)),
        -1 if d else +1,
        0 if d else len(m) - 1,
    )
    for i in rng:
        m[i][n - 1] = m[i + it][n - 1] if i != bl else temp
    return m


for _ in range(int(input())):
    m, a = generar(int(input())), input().split()
    for i in a:
        m = (
            movx(m, int(i[1]), signo[i[-1]])
            if i[0] == "F"
            else movy(m, int(i[1]), signo[i[-1]])
        )
    print(
        str(m)
        .replace("[[", "")
        .replace(", ", "")
        .replace("][", "\n")
        .replace("]]", "\n")
    )
