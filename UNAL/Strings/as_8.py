with open('conversaciones.txt', 'r') as fichero: 
    for linea in fichero:
        o,c, l = 0,0, list(map(str,linea.replace("\n","").replace(",","").lower().split(" ")))
        for i in range(len(l)-1):
            if l[i] in ["sin","no","ahora","aun"] and l[i+1] in ["embargo","obstante","bien","asi"]: o +=1
            if l[i] in ["por","dado","asi"] and l[i+1] in ["tanto","que","consiguiente","pues","ende"]: c +=1
        print("Opositivos "+str(o)+" Causativos "+str(c))