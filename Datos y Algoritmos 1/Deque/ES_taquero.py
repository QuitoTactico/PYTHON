from collections import deque  # IMPORTO DOUBLE-ENDED QUEUE

clientes = deque()  # INICIALIZADOR DE LISTA
tacos_vendidos = 0  # CONTADOR DE VENTAS
for _ in range(int(input())):  # N OPERACIONES A REALIZAR
    orden = deque(
        map(int, input().split(" "))
    )  # INPUT, PUEDE TENER 1 O 2 ENTEROS. EL PRIMERO ES LA FUNCIÓN
    if orden[0] == 1:
        clientes.append(orden[1])  # AÑADIR ORDEN
    if orden[0] == 2:
        tacos_vendidos += clientes.popleft()  # ELIMINAR ORDEN Y SUMARLA AL CONTADOR
    if orden[0] == 3:
        print(len(clientes))  # IMPRIME CUÁNTOS CLIENTES HAY EN FILA
    if orden[0] == 4:
        print(tacos_vendidos)  # IMPRIME CUÁNTOS TACOS SE HAN VENDIDO
    if orden[0] == 5:
        print(list(clientes))  # [EXTRA] IMPRIME TODAS LAS ORDENES QUE HAY EN FILA
