d = {}
def magic(m):
    c = sum(m[0])
    for i in m:
        if c != sum(i): return "Cuadrado muggle"
    for j in range(4):
        temp = 0
        for k in range(4): temp += m[j][k]
        if temp != c: return "Cuadrado muggle"
    return "Cuadrado muggle" if sum([m[0][0],m[1][1],m[2][2],m[3][3]]) != c or sum([m[0][3],m[1][2],m[2][1],m[3][0]]) != c else "Cuadrado magico"
n = int(input())
for _ in range(n):
    s , m= input().replace(":","").split() , []
    for _ in range(4): m.append(list(map(int,input().split())))
    d[int(s[1])] = magic(m)
for r in range(n): print(d[r+1])