def p(n):
    c = 0
    for i in range(1,n): 
        if n%i == 0: c+=i
    return str(n)+' es perfecto' if c == n else str(n)+" no es perfecto"
for i in range(int(input())): print(p(int(input())))