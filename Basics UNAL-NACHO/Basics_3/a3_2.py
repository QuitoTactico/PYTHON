# def l(n): return 2 if n == 1 else (1 if n == 2 else l(n-1)+l(n-2))


def f(n, m):
    s = [
        2,
        1,
        3,
        4,
        7,
        11,
        18,
        29,
        47,
        76,
        123,
        199,
        322,
        521,
        843,
        1364,
        2207,
        3571,
        5778,
        9349,
        15127,
        24476,
        39603,
        64079,
        103682,
        167761,
        271443,
        439204,
        710647,
        1149851,
        1860498,
        3010349,
        4870847,
        7881196,
        12752043,
    ]
    # for k in range(1,36): s.append(l(k))
    c = 0
    for i in range(n, m + 1):
        if i in s:
            c += 1
    return c


print(f(int(input()), int(input())))
# print(l(int(input())))
