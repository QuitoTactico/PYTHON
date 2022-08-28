from collections import defaultdict
l, d = [], defaultdict(lambda: [])
for _ in range(int(input())):
    e = input().split(", ")
    imc = round(float(e[1]) / float(e[2])**2 , 1)
    if imc > 25 and float(e[3]) > 100 and float(e[4]) > 150:
        l.append(imc)
        d[imc].append(e[0])
        d[imc] = sorted(d[imc],reverse= True)
c = 1
for i in sorted(l, reverse=True):
    print(str(c) +" "+ d[i][0] +" "+ str(i))
    d[i].pop(0)
    c += 1