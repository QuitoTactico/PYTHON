def islas(matriz):     
    num_islas = 0                           # INICIALIZAR CONTADOR
    filas = len(matriz)
    columnas = len(matriz[0])               # DIMENSIONES DE LA MATRIZ, PARA RECORRERLAS

    for Y in range(0,filas,1):            
        for X in range(0,columnas,1):       # ITERADORES PARA RECORRER LA MATRIZ (IZQ -> DER , ARR -> ABJ)

            if matriz[Y][X] == 0:           # ES AGUA, SALTARSE EL SIGUIENTE IF LO HACE MÁS RÁPIDO
                continue
            if matriz[Y][X] == 1:           # SI ESA POSICIÓN ES TIERRA, SIGNIFICA QUE HACE PARTE DE UNA ISLA NUEVA
                num_islas = num_islas + 1   # AUMENTA EL CONTADOR DE ISLAS
                matriz = eliminador_de_islas(matriz, Y, X)   # PORQUE YA LA CONTÓ, PARA NO CONTARLA 2 VECES
    return num_islas

def eliminador_de_islas(matriz, Y, X):  
    matriz[Y][X]  = 0
    filas = len(matriz)                 # DIMENSIONES DE LA MATRIZ, PARA ASEGURARSE DE QUE NO LAS SOBREPASE
    columnas = len(matriz[0])
    for iter_Y in range(-1,2,1):        # ITERADORES PARA QUE EJECUTE EN UN RADIO DE 1 ESPACIO
        for iter_X in range(-1,2,1):    # EL RANGE RETORNA [-1,0,1], EL FOR LO RECORRE Y LOS COLOCA EN LOS ACTUALES
            Y_actual = Y + iter_Y
            X_actual = X + iter_X       # COLOCA LOS ITERADORES EN EL X y Y A EJECUTAR (A CONVERTIR EN 0)

            if -1 < Y_actual < filas:
                if -1 < X_actual < columnas:   # PARA QUE LA POSICIÓN A EJECUTAR NO SOBREPASE LOS LÍMITES
                    if matriz[Y_actual][X_actual] == 1: 
                        eliminador_de_islas(matriz, Y_actual, X_actual) # ELIMINA EL RESTO DE LA ISLA, LO QUE SEA TIERRA
    return matriz   # CONVIRTIÓ LA MATRIZ, LA RETORNA YA SIN ESA ISLA


M = [[1,1,1,1,1],
     [0,1,0,0,0],
     [1,0,0,1,1],
     [0,0,0,0,1],
     [1,0,1,1,1]]

print(islas(M))