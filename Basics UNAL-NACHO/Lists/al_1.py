import datetime


def diferencia(s1, s2):
    d1 = datetime.datetime.strptime(s1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(s2, "%Y-%m-%d")
    dif = d2 - d1
    print(
        f"{dif.days} dias = {int(dif.total_seconds()//3600)} horas = {int(dif.total_seconds()//60)} minutos = {int(dif.total_seconds())} segundos"
    )


for _ in range(int(input())):
    s = input().split()
    diferencia(s[1], s[2])
