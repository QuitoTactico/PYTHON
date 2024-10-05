import collections


def mensaje(s):
    pila = collections.deque()
    c = 0
    for i in range(len(s)):
        if s[i] == "(":
            pila.append("(")
        if s[i] == ")" and len(pila) != 0:
            pila.pop()
            c = c + 2
    return c


print(mensaje(")()())"))
