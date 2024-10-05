from collections import defaultdict

d, p = defaultdict(lambda: 0), []
with open("discurso.txt", "r") as fichero:
    for linea in fichero:
        temp = []
        for i in (
            linea.lower()
            .replace(".", "")
            .replace(",", "")
            .replace("?", "")
            .replace(";", "")
            .replace(":", "")
            .split()
        ):
            if len(i) > 4:
                if i not in p:
                    p.append(i)
                if i not in temp:
                    temp.append(i)
        for h in temp:
            d[h] += 1
for m in sorted(p):
    print(f"{m} {d[m]}")
