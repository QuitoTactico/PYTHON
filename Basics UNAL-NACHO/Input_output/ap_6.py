n,res = int(input()),1
for i in [7,5,3,2]:
    if n%i == 0: res = i
if res == 1: print(f'{n} no es multiplo de ninguno de los primeros cuatro primos')
else: print(f'{n} es multiplo de {res}')