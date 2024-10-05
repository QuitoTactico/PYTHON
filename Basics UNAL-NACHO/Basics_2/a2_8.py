def f(n):
    return 1 if n == 0 else n * f(n - 1)


def p(n: str):
    c = 0
    for i in n:
        c += f(int(i))
    return str(n) + " es fuerte" if c == int(n) else str(n) + " no es fuerte"


for i in range(int(input())):
    print(p(input()))
