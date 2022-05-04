revistah = {}

n,m = map(int, input().split())
revista = list(map(str, input().split()))
nota = list(map(str, input().split()))

if m > n: 
    print("No")
    quit()

for i in revista: revistah[i] = 0
for i in revista: revistah[i] = revistah[i] + 1

res = "Si"
for i in nota: 
    if i not in revistah: 
        res = "No"
        continue
    if revistah[i] == 0:
        res = "No"
        continue
    revistah[i] = revistah[i] - 1


print(res)
