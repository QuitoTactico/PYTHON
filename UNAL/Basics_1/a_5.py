l1,l2 = [],[]

n = int(input())
for i in range(n):
    l1.append(int(input()))

for i in range(n):
    l2.append(int(input()))

l1.sort()
l2.sort()
l2.reverse()

c = n*2

for i in range(len(l1)):
    if l1[i]%2==1 and l2[i]%2 == 1  :c -= 2
    if l1[i]%2==0 and l2[i]%2 == 0  :c -= 2
       
print("Sobreviven "+str(c)+" soldados")