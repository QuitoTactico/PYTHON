revistah,notah = {}, {}

#n,m = map(int, input().split())
revista = list(map(str, input().split()))
nota = list(map(str, input().split()))

#print(n)
#print(m)
print(revista)
print(nota)

for i in revista:
    revistah[i] = 0


res = "Si"
for i in nota: 
    if i not in revistah:
        res = "No"

print(revistah)

print(res)
