def f(a: int, b: int):
    if b > a:
        exit()
    print(b)
    f(a, b + 2)


a = int(input())
if a == 0:
    print(0)
else:
    f(a, 2)
