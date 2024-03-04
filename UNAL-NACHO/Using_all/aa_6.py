from datetime import datetime
for _ in range(int(input())):
    s, last, dif, es = input().split(', '), 0, None, True
    for _ in range(int(s[1])):
        act = datetime.strptime(input(),'%Y-%m-%d')
        if last != 0 :
            diftemp = act - last
            if dif == None: dif, last = diftemp, act ; continue
            if diftemp != dif : es = False
            dif = diftemp
        last = act
    if es == False: print(f'{s[0]} no es asesino(a) serial periodico\n');continue
    print(f'{s[0]} ataca cada {dif.days} dias y volvera a hacerlo en {(last+dif).strftime("%Y-%m-%d")}\n')