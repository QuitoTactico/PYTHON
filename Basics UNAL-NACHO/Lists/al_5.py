from datetime import datetime

c, n = datetime.strptime("00:00:00", "%X") - datetime.strptime("00:00:00", "%X"), 0
for _ in range(int(input())):
    s = input().split(", ")
    if s[1] == "barberia":
        temp, n = datetime.strptime(s[3], "%X") - datetime.strptime(s[2], "%X"), n + 1
        c += temp
print(
    f"{n} veces\n{int((c.total_seconds()/(n))//3600)} horas, {int(((c.total_seconds()/(n))%3600)//60)} minutos, {int(((c.total_seconds()/(n))%3600)%60)} segundos"
)
