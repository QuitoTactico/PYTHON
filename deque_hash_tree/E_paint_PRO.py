def paintUWU(matriz, Y, X, ini, end):  
    matriz[Y][X] = end
    filas,columnas=len(matriz),len(matriz[0]) # DIMENSIONES DE LA MATRIZ, PARA ASEGURARSE DE QUE NO LAS SOBREPASE
    for iter_Y in range(-1,2,1):        # ITERADORES PARA QUE EJECUTE EN UN RADIO DE 1 ESPACIO
        for iter_X in range(-1,2,1):    # EL RANGE RETORNA [-1,0,1], EL FOR LO RECORRE Y LOS COLOCA EN LOS ACTUALES
            Y_actual = Y + iter_Y
            X_actual = X + iter_X       # COLOCA LOS ITERADORES EN EL X y Y A EJECUTAR (A CONVERTIR EN END)

            if -1 < Y_actual < filas and -1 < X_actual < columnas:   # PARA QUE LA POSICIÓN A EJECUTAR NO SOBREPASE LOS LÍMITES
                if matriz[Y_actual][X_actual] == ini: paintUWU(matriz, Y_actual, X_actual,ini,end)   # PINTA EL RESTO DE LA ZONA
    return matriz   # CONVIRTIÓ LA MATRIZ, LA RETORNA YA PINTADA

try:
    Y,X = map(int,input().split())     # Si da problemas, usa Y+1 y X+1 (posiciones malas, las reales a ojo)
    ini,end = map(str,input().split())
    YM,XM = map(int,input().split())
    M = []
    for i in range(YM): M.append(list(map(str,input().split())))

    if 0 <= Y < YM and 0 <= X < XM:
        if M[Y][X] == ini :  
            print(paintUWU(M,Y,X,ini,end))
            quit()
    print(M)
except: pass    #O print([])