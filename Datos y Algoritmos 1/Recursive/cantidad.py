def cantidad(s: str, n: int):
    if n == len(s):
        return 0
    if s[n] == "x":
        return cantidad(s, n + 1) + 1
    return cantidad(s, n + 1)


s = input()
print(cantidad(s, 0))
