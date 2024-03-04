def equilibra(personas):
    ordenado=sorted(personas)
    longitud=len(personas)
    ultimaPosicion=longitud-1
    return equilibradito(personas,0,ultimaPosicion)


def equilibradito(personasss,contador,ultimaPos):
    sumaTotal=sum(personasss)
    promedio=sumaTotal/2
    longitudd=(len(personasss))
    a1=[]
    b1=[]
    
    if contador==longitudd/2 or ultimaPos==longitudd/2:
        return (a1,b1)
    else:
        if sum(a1) or sum(b1) == promedio:
            return (a1,b1)
        else:
            if sum(a1)<=sum(b1):
                a1.append(personasss[contador])
                a1.append(personasss[ultimaPos])
                return equilibradito(personasss,contador+1,ultimaPos-1)
            elif sum(b1)<=sum(a1):
                b1.append(personasss[contador])
                b1.append(personasss[ultimaPos])
                return equilibradito(personasss,contador+1,ultimaPos-1)

a = [80, 59,60,81,57,58,76,75]

print(equilibra(a))