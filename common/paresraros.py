def f(a:int,b:int):
    if(b>a):
        return 0
    if(b != 6 and b!= 8):
        print(b)
    f(a,b+2)

a = int(input())
if a==0:
    print(0)
else:
    f(a,2)