l = []

while True:
    a = int(input())
    if a == 0:
        break
    l.append(a)

l.sort()

print(round((l[-3] - l[2]) / len(l) ** 2, 2))
