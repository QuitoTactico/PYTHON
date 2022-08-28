'''def mascorrupto(a: list):
    m = 0
    if (a[1] < a[3]):
        m = 2
    if (a[m+1] < a[5]):
        m = 4

    return a[m]'''

def mascorrupto(a: list):
    m=f(a,1,3,0)
    n=f(a,m,5,m)
    return a[n]

def f(a:list,b:int,c:int,m:int):
    if (a[b] < a[c]): 
        if c==3: return 2
        if c==5: return 4
    return m
