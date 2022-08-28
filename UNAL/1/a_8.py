n = int(input())
l = [0] * (n+1)
l[0] = 1
for i in range(n-1):l[int(input())] += 1
for i in range(len(l)):
    if l[i] == 0: print("La ficha faltante es la " + str(i))