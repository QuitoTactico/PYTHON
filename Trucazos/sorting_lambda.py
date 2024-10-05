def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a
