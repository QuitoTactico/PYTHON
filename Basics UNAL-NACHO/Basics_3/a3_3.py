def p(n: str):
    c = 0
    for i in n:
        c += int(i) ** len(n)
    return str(n) + " es Armstrong" if c == int(n) else str(n) + " no es Armstrong"


for i in range(int(input())):
    print(p(input()))
