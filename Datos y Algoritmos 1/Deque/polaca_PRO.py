from collections import deque

"""ME DICE QUE DEQUE NO TIENE INSERT :("""
pila = list(map(str, input().split(" ")))


i = 0
while len(pila) != 1:
    while len(pila) != 1:
        if pila[i] == "+":
            temp = float(pila[i - 1]) + float(pila[i - 2])
            break
        if pila[i] == "-":
            temp = float(pila[i - 2]) - float(pila[i - 1])
            break
        if pila[i] == "*":
            temp = float(pila[i - 1]) * float(pila[i - 2])
            break
        if pila[i] == "/":
            temp = float(pila[i - 2]) / float(pila[i - 1])
            break
        i = i + 1

    del pila[i - 2]
    del pila[i - 2]
    del pila[i - 2]
    pila.insert(i - 2, temp)
    i = 0

if pila[0] == pila[0]:
    print(int(pila[0]))
else:
    print(pila[0])
