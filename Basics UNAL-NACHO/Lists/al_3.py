import random
def juegodados(p):
    h = random.randint(1,6) + random.randint(1,6)
    res = "Gana el humano" if h>p else "Gana la plataforma" if h<p else "Empate"
    print(res)
for _ in range(int(input())): juegodados(int(input().split()[1]))