def suporinf(m,n) -> bool:
    for i in range(len(m)):
        r = range(i) if n == 1 else range(i+1,len(m))
        for j in r:
            if m[i][j] != 0: return True
    return False
for _ in range(int(input())):
    m = []
    for _ in range(int(input())): m.append(list(map(float,input().split())))
    sup, inf = suporinf(m,0) , suporinf(m,1)
    res = 'Ni diagonal ni triangular' if sup == True and inf == True else 'Triangular superior' if sup == True and inf == False else 'Triangular inferior' if sup == False and inf == True else 'Diagonal'
    print(res)