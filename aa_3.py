def cameos(linea) -> int:  #Así se pone la documentación de métodos que retornan ;)
    c, l = 0, 'saramago'
    for i in linea:
        if i == l[0]: l = l[1:]
        if len(l) == 0: c, l = c+1, 'saramago'
    return c
with open('cameos.txt', 'r') as fichero: 
    for linea in fichero: print(cameos(linea.lower()))