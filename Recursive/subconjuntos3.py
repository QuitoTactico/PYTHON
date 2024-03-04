def subconjuntos(s):
    subconjuntosAux(s[:-2], s[-2:])
    
def subconjuntosAux(a:str,b:str):
    print(a+b)
    print(a+b[0])
    print(a+b[1])
    print(a)



subconjuntos(input())