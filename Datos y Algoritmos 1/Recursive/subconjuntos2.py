def subconjuntos(s):
    subconjuntosAux(s[:-2], s[-2:],2)
    subconjuntosAux(s[:-3], s[-2:],2)
    subconjuntosAux(s[:-4]+s[-3], s[-2:],2)
    subconjuntosAux(s[:-4],s[-2:],2)
    
def subconjuntosAux(a:str,b:str,c:int):
    if (c==0):
        print("-")
    else:
        print(a+b)
        print(a+b[0])
        print(a+b[1])
        print(a)

        
        #if(len(a)>1):subconjuntosAux(a[:-2]+a[-1],b)
        #if(len(a)>0):subconjuntosAux(a[:-2],b)


        #s = a+b
        #subconjuntos(s[1:])
        c = c-1

s = str(input())     
subconjuntos(s)     #asdas a todos
if(len(s)==5): subconjuntos(s[1:])  #sdas  s final  todos
#subconjuntos(s[2:])
#subconjuntos(s[3:])

#print((s[3:])[-1])