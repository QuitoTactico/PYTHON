#c

import collections
tacos = collections.deque()
impresiones = collections.deque()
c = 0
for _ in range(int(input())):
    str_input = input()
    if len(str_input) == 1: func = int(str_input)
    else: func,clienteNuevo = map(int,input().split())

    if func == 1: tacos.append(clienteNuevo)

    if func == 2: c =+ tacos.popleft()


    if func == 3: print(len(tacos))

    if func == 4: print(c)
