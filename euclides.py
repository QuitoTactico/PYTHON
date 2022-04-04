#lit es maximo comun divisor
def bal(a: int, b :int):
    if b==0: return a
    return bal(b,a%b)

idk = int(input())

#for i in range(1,idk+1,1):
#    a, b = map(int, input().split())
#    print("Case "+str(i)+": "+str(bal(a,b)))

def f(n:int,c:int):
    if(c==n): return
    a, b = map(int, input().split())
    print("Case "+str(c)+": "+str(bal(a,b)))
    f(n,c+1)
f(idk+1,1)


