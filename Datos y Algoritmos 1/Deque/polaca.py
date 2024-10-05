import collections

pila = collections.deque(map(str, input().split(" ")))

print(pila)

i = 0
while len(pila) != 1:
    while len(pila) != 1:
        if pila[i] == "+":
            temp = eval(pila[i - 1]) + eval(pila[i - 2])
            break
        if pila[i] == "-":
            temp = eval(pila[i - 1]) - eval(pila[i - 2])
            break
        if pila[i] == "*":
            temp = eval(pila[i - 1]) * eval(pila[i - 2])
            break
        if pila[i] == "/":
            temp = eval(pila[i - 1]) / eval(pila[i - 2])
            break
        i = i + 1

    del pila[i - 2]
    del pila[i - 2]
    del pila[i - 2]
    pila.insert(i - 2, temp)
    i = 0
    print(pila)


print(pila[0])
