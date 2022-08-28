d = {}
for _ in range(int(input())):
    t = input().split()
    d[t[0]] = t[1]
for _ in range(int(input())):
    o = input()
    if o in d: print(d[o])
    else: print("palabra no encontrada")