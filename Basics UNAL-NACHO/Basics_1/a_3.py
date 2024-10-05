d = []
c = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a not in d:
        d.append(a)
        c += 1

print(c)
