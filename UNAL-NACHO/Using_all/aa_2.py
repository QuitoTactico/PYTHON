from datetime import datetime
anterior, sumatoria, n = None,0, int(input())
def formato(dif): 
    d = int(dif/86400)
    dif %= 86400
    h = int(dif/3600)
    dif %= 3600
    m = int(dif/60)
    sec = int(dif%60)
    return f'{d} dias, {h} horas, {m} minutos, {sec} segundos'
for _ in range(n):
    s = datetime.strptime(input(), '%Y-%m-%d %X')
    if anterior != None:  
        temp = s-anterior
        sumatoria += temp.total_seconds() 
        print(formato(int(temp.total_seconds())))
    anterior = s
print(f'\nPromedio: {formato(int(sumatoria/(n-1)))}')