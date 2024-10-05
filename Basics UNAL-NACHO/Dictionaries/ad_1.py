from collections import defaultdict

p = defaultdict(lambda: [])
for _ in range(int(input())):
    s = input().split()
    if s[2] == "positiva":
        p[int(s[3])] = sorted(p[int(s[3])] + [int(s[1])], reverse=True)
for i in range(10, -1, -1):
    if i in p:
        for j in p[i]:
            print(str(j) + " POSITIVA " + str(i))
