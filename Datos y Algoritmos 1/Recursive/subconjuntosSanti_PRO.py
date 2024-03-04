def llamado(sabores):
    return subcon([],sabores)

def subcon(act,conj):
    if conj:
        return(subcon("".join(act)+"".join([conj[0]]),"".join(conj[1:])) + subcon("".join(act),"".join(conj[1:])))
    return([act])

def imprimir(resultado,i):
    if(i<len(resultado)):
        print (resultado[i])
        return imprimir(resultado,i+1)
        

palabras=str(input())     # QUÉ QUIERES QUE TE COMBINEN?
sabores=list(palabras)    # LO QUE QUIERES PERO EN LISTA
resultado=llamado(sabores)# LO MANDA Y RETORNA UNA LISTA CON LAS COMBINACIONES
#imprimir(resultado,0)    SI QUIERE QUE LE IMPRIMAN LAS COMBINACIONES, LINEA PA CADA UNO
#print(resultado)         SI QUIERE QUE LE IMPRIMAN LA LISTA CON LAS COMBINACIONES, ["ASDAS","ASDA","ASDS"...]