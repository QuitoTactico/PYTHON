# Funcion que lee cada input y los agrega en un arreglo
caracteres = [str(x) for x in input().split()]


def f(l: list, c: int):
    if len(l) == c:
        return
    h = l.copy()
    h.pop(c)
    g(l[c], h)
    f(l, c + 1)


def g(s: str, l: list):
    print(s + l[0] + l[1])
    print(s + l[1] + l[0])


# f(caracteres,0)
str = caracteres[0]
# caracteres.pop(0)
# print(ll)
if len(caracteres) == 2:
    g("", caracteres)
else:
    f(caracteres, 0)
# print(caracteres)
