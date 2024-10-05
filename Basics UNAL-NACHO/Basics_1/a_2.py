lb, lr = [], []

n = int(input())
for i in range(n):
    lb.append(int(input()))

for i in range(n):
    lr.append(int(input()))

cb = 0
cr = 0

for i in range(len(lb)):
    if lb[i] > lr[i]:
        cb += 2
    if lb[i] < lr[i]:
        cr += 2
    if lb[i] == lr[i]:
        cb += 1
        cr += 1


print("Ballenota Futbol Club: " + str(cb))
print("Real Mandril: " + str(cr))
