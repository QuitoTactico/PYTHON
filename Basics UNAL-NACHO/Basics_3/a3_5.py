l = []
for i in range(int(input())):
    l.append(float(input()))
s = l.copy()
s.sort()
for i in s:
    print(l.index(i) + 1)
