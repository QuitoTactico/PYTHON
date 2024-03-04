v,l = [0] * 5000  , []
basurazzz = input()
for i in range(int(input())): l.append(int(input()))
for i in l: v[i] += 1
m = max(v)
for i in range(len(v)):
    if v[i] == m: print(i)