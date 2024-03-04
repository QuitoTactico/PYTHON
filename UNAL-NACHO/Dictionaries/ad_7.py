from collections import defaultdict
d, m, v = defaultdict(lambda:0), 0, ""
for _ in range(int(input())):
    s = input().split(": ")
    d[s[0]] += int(s[1])
    if d[s[0]] > m: m, v = d[s[0]] , s[0]
print(f"El vendedor del mes es {v}")