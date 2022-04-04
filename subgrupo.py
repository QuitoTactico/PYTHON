def f(n:int,list:list,c:int) -> int :
    if(c==n): return 1
    if(c>n): return 0
    h(n,list,c,int(len(list))-1,0)
    #for j in range(0,int(len(list))-1,1):
    #    return f(n,[list.pop(j)],c+list[j])

def g(r:int) -> str:
    if((r==0)):return "NO"
    return "YES"

def h(n:int,list:list,c:int,l:int,cc:int):
    if cc==l:return
    h(n,list,c,l,cc+1)
    return f(n,[list.pop(cc)],c+list[cc])


e, n = map(int,input().split())
list = list(map(int,input().split(" ")))
if(e==0):
    print("NO")
    quit()
    
print(g(f(n, list ,0)))