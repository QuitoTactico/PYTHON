from datetime import datetime
for _ in range(int(input())):
    s,st = input().split(), ""
    i, f = datetime.strptime(s[0],"%d-%m-%Y"),datetime.strptime(s[1],"%d-%m-%Y")
    d = f-i
    for _ in range(int(d.days//5)): st += "5 "
    for _ in range(int(d.days%5)): st += "1 "
    print(st[:-1])