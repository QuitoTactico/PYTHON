for _ in range(int(input())): 
    c = 0
    for i in input().replace(" ",""): c = c+1 if i == "F" else c-1
    res = "Es posible hacer un unico circulo" if c == 0 else "No es posible"
    print(res)