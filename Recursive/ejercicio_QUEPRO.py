#ES EL MEJOR CARECHIMBA CÓDIGO QUE HECHO EN LA VIDA PS
#pana estoy muy feliz
#Reutilicé mucho de mi código de subconjuntos.py para hacer las combinaciones
def h(l:list,ll:list):
    #print(l)
    if(ll==[]):
        #print("gae")
        s=input()
        g(s,len(s),"",[],l)
    else:
        #print("gaen't")
        k(l,ll)

def k(l:list,ll:list):

    print(r(l,ll,0)) 
    return

def r(a,b,m):
    if(len(a)==0): return m
    return max(c(a[0],b,0),r(a[1:],b,m))

def c(a:str,b,m) -> int :
    if(len(b)==0):return m
    if(a==b[0]): m = max(m,len(a))
    return c(a,b[1:],m)   


def f(c:str,s:str,l:list,ll:list):
    if(len(s)<=1): h(l,ll)
    elif(len(s)==2):
        l.append(c+s)
        l.append(c+s[0])
        l.append(c+s[1])
        l.append(c)
    else:
        g(s[1:],len(s)-2,c+s[0],l,ll)

s = input()
def g(s,c,sc,l:list,ll:list):
    if(c!=0):
        f(sc,s,l,ll)
        g(s[1:],c-1,sc,l,ll)
g(s,len(s),"",[],[])