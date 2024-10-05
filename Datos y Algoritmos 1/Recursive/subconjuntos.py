# Que belleza de código nea
def f(c: str, s: str):
    if len(s) <= 1:
        pass
    elif len(s) == 2:
        print(c + s)
        print(c + s[0])
        print(c + s[1])
        print(c)
    else:
        g(s[1:], len(s) - 2, c + s[0])


s = input()
c = len(s)


def g(s, c, sc):
    if c != 0:
        f(sc, s)
        g(s[1:], c - 1, sc)


g(s, c, "")
