l = []
for i in range(int(input())):
    l.append(int(input()))

c1 = 0
c2 = 0 
c3 = 0 
c4 = 0
c5 = 0

for i in l:
    if i == 1: c1 += 1
    if i == 2: c2 += 1
    if i == 3: c3 += 1
    if i == 4: c4 += 1
    if i == 5: c5 += 1


print("1: " + str(c1))
print("2: " + str(c2))
print("3: " + str(c3))
print("4: " + str(c4))
print("5: " + str(c5))