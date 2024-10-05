def f(l: list):
    c, cl, cr = 0, 0, 0
    for i in range(1, len(l)):
        for n in range(0, i):
            cl += l[n]
        for m in range(i, len(l)):
            cr += l[m]
        if cl == cr:
            c += 1
        cl, cr = 0, 0
    return c


l = []
for i in range(int(input())):
    l.append(float(input()))
print(f(l))
