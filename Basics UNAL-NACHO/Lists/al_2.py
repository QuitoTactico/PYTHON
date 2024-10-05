from datetime import datetime

d = {
    "true vampires": 0,
    "early birds": 0,
    "sunny warmers": 0,
    "lunch workers": 0,
    "sunset lovers": 0,
    "prime timers": 0,
}
l = [
    "true vampires",
    "early birds",
    "sunny warmers",
    "lunch workers",
    "sunset lovers",
    "prime timers",
]
d1 = datetime.strptime("00:00:00", "%X").time()
d2 = datetime.strptime("04:00:00", "%X").time()
d3 = datetime.strptime("08:00:00", "%X").time()
d4 = datetime.strptime("12:00:00", "%X").time()
d5 = datetime.strptime("16:00:00", "%X").time()
d6 = datetime.strptime("20:00:00", "%X").time()
d7 = datetime.strptime("23:59:59", "%X").time()


def rangohoras(h):
    act = datetime.strptime(h, "%X").time()
    if d1 <= act < d2:
        d["true vampires"] += 1
    if d2 <= act < d3:
        d["early birds"] += 1
    if d3 <= act < d4:
        d["sunny warmers"] += 1
    if d4 <= act < d5:
        d["lunch workers"] += 1
    if d5 <= act < d6:
        d["sunset lovers"] += 1
    if d6 <= act <= d7:
        d["prime timers"] += 1


for _ in range(int(input())):
    rangohoras(input().split()[1])
for i in range(6):
    print(f"{l[i]} {d[l[i]]}")
