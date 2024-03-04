from random import randint
from datos import generarDatos
import matplotlib.pyplot as plt
import time
#-----------------------------------------------------------------------
def BubbleSort(lista : list) -> list:
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]< lista[j]: lista[i],lista[j] = lista[j],lista[i]
    return lista
#-----------------------------------------------------------------------
def QuickSort(datos):
    if len(datos) <= 1: return datos
    pivote = datos[len(datos)//2]
    izq = [x for x in datos if x < pivote]
    centro = [x for x in datos if x == pivote]
    der = [x for x in datos if x > pivote]
    return QuickSort(izq) + centro + QuickSort(der)
#-----------------------------------------------------------------------
def MergeSort(datos):
    if len(datos) <= 1: return datos
    if len(datos) == 2: return datos if datos[0] <= datos[1] else sorted(datos)
    mitad = len(datos) // 2
    return op_Merge( MergeSort(datos[:mitad]) , MergeSort(datos[mitad:]) )

def op_Merge(lx:list , ly:list):
    ix, iy, out = 0,0, []  #x = y = 0
    while ix < len(lx) and iy < len(ly):
        if lx[ix] < ly[iy]:
            out.append(lx[ix])
            ix += 1
        else:
            out.append(ly[iy])
            iy += 1
    return out + lx[ix:] + ly[iy:]
#-----------------------------------------------------------------------
def PythonSort(datos): return sorted(datos)
#=======================================================================

def temporizador(n:int,b:int):
    d = []
    
    ini = time.time()
    lista = generarDatos(n)
    fin = time.time()
    d.append(fin-ini)


    if n <= b:
        ini = time.time()
        temp = BubbleSort(lista)
        fin = time.time()
        d.append(fin-ini)
    else: d.append(None)

    ini = time.time()
    temp = MergeSort(lista)
    fin = time.time()
    d.append(fin-ini)

    ini = time.time()
    temp = QuickSort(lista)
    fin = time.time()
    d.append(fin-ini)


    ini = time.time()
    temp = PythonSort(lista)
    fin = time.time()
    d.append(fin-ini)

    return d

if __name__ == '__main__':
    fig, ax = plt.subplots()
    generacion,bubble,merge,quick,python_sort = [],[],[],[],[]

    '''CAMBIA EL L PARA LOS VALORES QUE QUIERAS EVALUAR.'''
    '''CAMBIA EL 0 DE TEMPORIZADOR PARA EJECUTAR EL BUBBLE'''
    #l = [100,500,1000,5000,10000,25000,50000] + list(range(100000,1000001,50000))
    l= list(range(0,100001,5000))

    for i in l:
        d = temporizador(i,0)
        generacion.append(d[0])
        bubble.append(d[1])
        merge.append(d[2])
        quick.append(d[3])
        python_sort.append(d[4])

    ax.set_xlabel("Número de Datos", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel("Tiempo de Ejecución", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:orange'})

    ax.plot(l,generacion,label = 'Generación Datos')
    ax.plot(l,bubble,label = 'Bubble Sort')
    ax.plot(l,merge,label='Merge Sort')
    ax.plot(l,quick,label='Quick Sort')
    ax.plot(l,python_sort,label='Python Sort')

    ax.legend(loc = 'upper left')

    plt.show()
    


    

#print(temporizador(5000))


'''
ini = time.time()
fin = time.time()
d[''] = fin-ini

'''


