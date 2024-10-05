def last_digit(lst):
    nada = [None, []]
    if lst in nada:
        return 1

    res = lst[0] % 10
    for i in lst[1:]:
        for _ in range(i):
            res = (res * res) % 10
    return res


# -------------------------------------------------------------


def last_digit_of_power(a, b):
    if b == 0:
        return 1

    a %= 10
    if a in [0, 1, 5, 6]:
        return a
    if a in [4, 9]:
        return 4 if b % 2 == 0 else a
    if a in [2, 3, 7, 8]:
        b = b % 4 if b % 4 != 0 else 4
        return (a**b) % 10


def last_digit2(lst):
    if not lst:
        return 1
    power = 1
    for x in reversed(lst):
        power = last_digit_of_power(x, power)
    return power


# --------------------------------------------------------------------


def last_digit_of_power(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 5:
        return 5
    if a == 6:
        return 6
    if a == 9:
        return 9 if b % 2 == 1 else 1
    if a == 4:
        return 4 if b % 2 == 1 else 6

    # ciclos de 4
    a = a % 10
    cycle = [a, (a**2) % 10, (a**3) % 10, (a**4) % 10]
    return cycle[(b % 4) - 1]


def last_digit(lst):
    if not lst:
        return 1

    power = 1
    for x in reversed(lst):
        if power == 0:
            power = 1
        else:
            power = last_digit_of_power(x, power)

    return power


# ------------------------------------------------------------------------------


def last_digit(lst):
    if not lst:
        return 1

    def mod4(x):
        if x == 0:
            return 0
        return (x % 4) + 4

    def last_digit_of_power(a, b):
        if b == 0:
            return 1
        if a == 0:
            return 0

        a %= 10
        if a in [0, 1, 5, 6]:
            return a
        if a in [4, 9]:
            return 4 if b % 2 == 1 else 6 if a == 4 else 1
        if a in [2, 3, 7, 8]:
            b = mod4(b)
            return (a**b) % 10

    power = 1
    for x in reversed(lst):
        power = last_digit_of_power(x, power)

    return power


# print(last_digit([3, 4, 2]))
