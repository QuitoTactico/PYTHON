def h(n:str):
    for i in n:
        if int(i) % 2 == 1:return('No es hyperpar')
    return("Hyperpar")
    
while(True):
    n = input()
    if n == "-1": break
    print(h(n))