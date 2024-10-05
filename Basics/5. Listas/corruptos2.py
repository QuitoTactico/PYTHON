def mascorrupto(a: list):
    m = 0
    if a[1] < a[3]:
        m = 2
    if a[m + 1] < a[5]:
        m = 4

    return a[m]
