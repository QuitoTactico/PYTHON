l = [0] * 142
for i in range(142): l[i] = int(((i*(i+1))/2))
while True:
    a = int(input())
    if a == 0 : break
    if a in l: print("Puede ser un racimo ideal")
    if a not in l: print("No puede ser un racimo ideal")