def f(n):
    for i in range(n):
        for j in range(n):
            if j in [i,n-i-1]: print("#",end="")
            else: print(0,end="")
        print()
    print()
while(True):
    n = int(input())
    if n == 0: break
    else:f(n)