from collections import defaultdict, deque

def extension(arreglo,k):
    if arreglo == None : arreglo = []
    diferencias = defaultdict(lambda: 0)
    arreglo = deque(arreglo)

    for _ in range(len(arreglo)):
        for i in range(1,len(arreglo)):  diferencias[abs(arreglo[0]-arreglo[i])] += 1
        arreglo.popleft()

    return diferencias[k]


l = (10,20,30,40,50,50,1000,1030,1000,1010,1040)

print(extension(None,7))
