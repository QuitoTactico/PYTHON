def f(n):
    l = []
    for i in n:
        if int(i) in [1, 2, 3, 4, 5] and int(i) not in l:
            l.append(int(i))
    l.sort()
    return "Multidigito" if l == [1, 2, 3, 4, 5] else "No es multidigito"


while True:
    n = input()
    if n == "0":
        break
    else:
        print(f(n))
