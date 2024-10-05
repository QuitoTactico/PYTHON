def mascorrupto(a: list):
    m = 0
    if a[1] < a[3]:
        m = 2
    if a[m + 1] < a[5]:
        m = 4

    return a[m]


def g(a: list, m):
    g(a[1:], m)


def f(a: list, c, m):
    if c == 2:
        return 0
    if a[1] < a[3]:
        m = 3
    else:
        m = 1
    return max(f(a), f(a[1:]))


def h(a: list, m, c):
    if c == 2:
        return a[m - 1]
    if a[2 * c] < a[2 * c + 2]:
        m = m + 2
    return h(a, m, c + 1)


l = ["Calvarini", 10000, "Pinturosky", 2000, "Tajardini", 4000000]
print(h(l, 1, 0))
