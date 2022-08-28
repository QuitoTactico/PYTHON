from collections import deque
from random import randint
for _ in range(int(input())):
    c, h, p, humn, plat = list(range(1,14))*4 , 0 , 0, deque(), deque(map(int, input().split()[1:]))
    try: 
        for i in plat: c.remove(i)
    except: ""
    for j in range(10):
        a = randint(0,len(c)-1)
        humn.append(c.pop(a))
    for _ in range(10):
        ch, cp = humn.pop(), plat.pop()
        h,p = h+1 if ch>cp else h , p+1 if cp>ch else p
    print(f"Puntos humano: {h} Puntos plataforma: {p}")