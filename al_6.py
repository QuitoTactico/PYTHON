from datetime import datetime
for _ in range(int(input())):
    s,c = input().split(), 0
    for i in range(int(s[1])):
        if datetime.strptime(f"{int(s[0][:4])+i+1}{s[0][4:]}","%Y/%m/%d").weekday() == 0: c += 1
    print(c)