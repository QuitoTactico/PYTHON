l = []
p = []
for i in range(int(input())):
    s = input().split()
    if s[2] == "positiva": 
        l.append({"pizza": s[3], "edad": s[1]})
        p.append(s[3])
p = sorted(p)
print(p)
print(l)