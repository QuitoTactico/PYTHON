def f(n:int,A:int,B:int,C:int,D:int):
    if n==1:
        print("Mover disco 1 de la vara",A,"a la vara",B)
        return
    f(n-1,A,C,B,D+1)
    print("Mover disco",n,"de la vara",A,"a la vara",B)
    f(n-1,C,B,A,D+1)
    
a=int(input())
f(a,1,3,2,0)
print((2**a)-1)