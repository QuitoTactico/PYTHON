l = []
while True:
    a = int(input())
    if a == 0 : break
    l.append(a)
c = 0
for n in l:
    for m in l:
        if n != m:
            if n + m == 1995: c += 1
print(int(c/2)) 