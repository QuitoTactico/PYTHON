from datetime import datetime
def reloj_porcentaje(h):
    hh, a = datetime.strptime(h,'%I:%M:%S %p') , datetime.strptime("00:00:00",'%X')
    print(F"Loading day ... {round((hh-a).total_seconds()/864,3)}%")
for _ in range(int(input())): reloj_porcentaje(input())