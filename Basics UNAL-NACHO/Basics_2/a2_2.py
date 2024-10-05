def f(n):
    return (2 + (5 * n)) ** 0.5


def g(n):
    return (4 + n) ** 3


while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        print(f(g(n)))
    else:
        print(g(f(n)))
