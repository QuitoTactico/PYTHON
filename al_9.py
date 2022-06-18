#Mi favorito hasta ahora
from datetime import datetime
mes = {1:"Enero",2:"Febrero",3:"Marzo",4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
def calendario(y, m):
    d , s = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} , datetime.strptime(f'1/{m}/{y}','%d/%m/%Y').weekday()
    d[2] = 29  if y%4 == 0 and (y%100 != 0 or y%400==0)else 28
    print('lun\tmar\tmie\tjue\tvie\tsab\tdom')
    for _ in range(s): print("\t",end="")
    for i in range(1,d[m]+1):
        if i != 1 and s!= 0: print(f"\t{i}",end="")
        else: print(i,end="")
        s += 1
        if s == 7:print();s=0
modo = int(input("Ingrese -1 para obtener el calendario de todo el año. -> "))
if modo == -1:
    a = int(input("Qué año?\n"))
    for i in range(1,13):
        print("___________________________________________________ "+mes[i])
        calendario(a,i)
        print()
else:
    for _ in range(modo):
        s = list(map(int,input().split("/")))
        calendario(s[2],s[1])
        print("\n")