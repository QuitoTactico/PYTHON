p, t = {}, []
for _ in range(int(input())):
    s = list(map(int, input().split(", ")))
    p[int(s[0])] = s[1:]
    t.append(s[0])
for k in p:
    for l in range(12):
        n = (
            8
            if l in [3, 7]
            else (
                9
                if l in [0, 5, 10]
                else 10 if l in [9, 11] else 11 if l in [1, 6, 8] else 12
            )
        )
        p[k][l] = round((p[k][l] / n) * 5, 1)
for i in sorted(t):
    print(str(i) + " " + str(round(sum(p[i]) / 12, 1)))
