from random import randint
from datos import generarDatos
import time

n = int(input())
# n = 10
"""lista = []
for _ in range(n):
    lista.append(randint(1,1000))"""

lista2 = generarDatos(n)


"""====================================================================="""

# the original bubble i know, de 2 en 2
"""def Burbuja1(l : list) -> list: 
    for _ in range(len(l)):
        for i"""

"""====================================================================="""


# comparando con la iteración mayor en la que esté
def Bubble2(lista: list) -> list:
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


"""====================================================================="""


# complicado al comparar con pivote
def QuickSort(datos):
    if len(datos) <= 1:
        return datos
    pivote = datos[len(datos) // 2]
    izq = [x for x in datos if x < pivote]
    centro = [x for x in datos if x == pivote]
    der = [x for x in datos if x > pivote]
    return QuickSort(izq) + centro + QuickSort(der)


"""====================================================================="""


#  U, and the real sort
def op_Merge(lx: list, ly: list):
    # indices
    ix, iy, out = 0, 0, []  # x = y = 0
    while ix < len(lx) and iy < len(ly):
        if lx[ix] < ly[iy]:
            out.append(lx[ix])
            ix += 1
        else:
            out.append(ly[iy])
            iy += 1
    return out + lx[ix:] + ly[iy:]


# complicado al reunir, pero se hace arriba
# just to cut
def MergeSort(datos):
    if len(datos) <= 1:
        return datos
    if len(datos) == 2:
        return datos if datos[0] <= datos[1] else sorted(datos)
    # impares izquierda mayor por 1
    mitad = len(datos) // 2
    # partir partir partir, dejar acumulados los op_merge, en donde realmente se ordenan las cosas al llegar a uno de los dos finales (1 o 2)
    return op_Merge(MergeSort(datos[:mitad]), MergeSort(datos[mitad:]))


"""====================================================================="""


if __name__ == "__main__":
    """print(lista)
    print(burbuja_2(lista))
    print(QuickSort(lista))"""

    # ORIGINAL
    # for i in lista2: print(i)
    print("\n________________________\n")

    inicio = time.time()
    l_quick = QuickSort(lista2)
    fin = time.time()

    # for i in l_quick: print(i)
    print(f"-> cantidad: {n} datos ({n == len(l_quick)})")
    print(f"-> tiempo:   {fin-inicio} s")

    inicio = time.time()
    l_merge = MergeSort(lista2)
    fin = time.time()

    # for i in l_merge: print(i)
    print(f"-> cantidad: {n} datos ({n == len(l_merge)})")
    print(f"-> tiempo:   {fin-inicio} s")
