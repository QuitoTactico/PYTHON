def f(s: str, a: int, b: int):
    if a == b:
        return
    print(s[a], end="")
    f(s, a + 1, b)


s = input()
a = int(input())
b = int(input())
f(s, a, b + 1)
