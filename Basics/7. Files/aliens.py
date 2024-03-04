abrir= (open("aliens.txt"))
lineas = abrir.readlines()
guardados = []
for line in lineas:
    guardados.append(line.split())

guardados2 = []
jj = 0
for j in guardados:
    sb = str(guardados[jj])
    num = sb[sb.find(",")+1:sb.find("'",sb.find(",")+1)]
    guardados2.append(int(num))
    jj = jj+1

mayor = 0
h = 0
for i in guardados2:
    if(guardados2[h] > guardados2[mayor]):
        mayor = h
    h = h+1

#sb = str(guardados[0])
#num = sb[sb.find(",")+1:sb.find("'",sb.find(",")+1)]

sa = str(guardados[mayor])
respuesta = sa[2:sb.find(",")]
print(respuesta)