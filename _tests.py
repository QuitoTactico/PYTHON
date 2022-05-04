import collections
from collections import defaultdict

def t1():
    pila = collections.deque([1,2,3])

    pila.pop()
    pila.pop()

    print(pila)

def t2():
    pila = collections.deque([1,2,3])

    pila.insert(1,3)

    print(pila)

def t3():
    print(5.1 == 5)

def t4():
    for i in range(-1,2,1):
        print(i)

def t5():
    a = defaultdict(lambda: "default", key="some_value")
    print(a["blabla"])
    print(a["key"])
    print(a["sapo"])

def t():
    a = defaultdict(lambda: 5)
    print(a["blabla"])
    print(a["key"])
    print(a["sapo"])
    a["sapo"] -= 1
    print(a["sapo"])

t()