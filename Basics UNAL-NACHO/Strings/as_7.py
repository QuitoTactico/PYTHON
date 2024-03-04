with open('cadena.txt', 'r') as fichero: 
    for linea in fichero:
        res, l = "cadena completa", list(map(str,linea.replace("\n","").split()))
        for i in range(len(l)-1):
            if l[i][-2:] != l[i+1][:2] and l[i][-3:] != l[i+1][:3] : res = "cadena rota" 
        print(res)