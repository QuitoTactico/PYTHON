abrir= (open("notas.txt"))
lineas = abrir.readlines()
guardados = []
for line in lineas:
    guardados.append(line.split())

a = list(guardados[0])
a1 = list(a[0])

a2 = []
for i in range(0,len(a1),2):
    a2.append(a1[i])

sum = 0
for j in range(0,len(a2),1):
    sum = sum + int(a2[j])

print(sum/5)