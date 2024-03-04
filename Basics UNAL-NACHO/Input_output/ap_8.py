l,d = [50000,20000,10000,5000,2000,1000],{50000:0,20000:0,10000:0,5000:0,2000:0,1000:0}
def verif(n):
    for i in l:
        if n>=i: d[i] += 1 ;return verif(n-i)
verif(int(input()))
for i in l:
    if d[i] != 0: print(f'{d[i]} de ${i}')