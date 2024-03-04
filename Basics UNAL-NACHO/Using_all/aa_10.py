def filas(m):       #DEMASIADO PRO
    for i in m:     #Mi segundo favorito
        for j in range(9):
            if i[j] in i[:j]: return False
    return True
def columnas(m):
    for i in range(9):
        l = []
        for j in range(9):
            if m[j][i] in l: return False
            else: l.append(m[j][i])
    return True
def regiones(m):
    for i in range(3):
        for j in range(3):
            if list(range(1,10)) != sorted(m[3*i][3*j:3*(j+1)]+m[(3*i)+1][3*j:3*(j+1)]+m[(3*i)+2][3*j:3*(j+1)]): return False
    return True
def revisar(m): return "Resuelto" if filas(m) and columnas(m) and regiones(m) else 'No resuelto'
for _ in range(int(input())):
    basuraestupida, m = input() , []
    for _ in range(9): m.append(list(map(int, input().split())))
    print(revisar(m))