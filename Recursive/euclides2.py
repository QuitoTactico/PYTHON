#lit es maximo comun divisor
def bal(a: int, b :int):
    if b==0: return a
    return bal(b,a%b)

idk = int(input())
for i in range(1,idk+1,1):
    a, b = map(int, input().split())
    print("Case "+str(i)+": "+str(bal(a,b)))