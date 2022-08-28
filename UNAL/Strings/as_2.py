for _ in range(int(input())): 
    l = list(map(str,input().split(" ")))
    res = "Mi cacharrito es el mas viejo de todos los autos ;D" if l[0] == sorted(l)[0] else "Al menos otro auto es mas viejo que mi cacharrito :("
    print(res)