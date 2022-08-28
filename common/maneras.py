def f(n:int,c:int) -> int :
    if(c==n): return 1
    if(c>n): return 0
    return f(n,c+3) + f(n,c+5) + f(n,c+7)

n = int(input())
print(f(n,0))