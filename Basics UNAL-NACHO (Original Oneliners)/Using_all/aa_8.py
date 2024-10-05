def camino(l:list,a,c):
    if a == 'C-137': return c
    for i in l:
        if i[0] == a: return camino(l,i[1],c+1)
    return -1
for _ in range(int(input())):
    a,l = None, []
    for _ in range(int(input())):
        if a == None: a = input().split()[1]
        else: l.append(input().split())
    n = camino(l,a,1)
    res = f'Pueden volver a C-137 en {n} saltos' if n!= -1 else 'Deambulan por el multiverso'
    print(res)