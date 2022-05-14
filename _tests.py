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

def t6():
    a = defaultdict(lambda: 5)
    print(a["blabla"])
    print(a["key"])
    print(a["sapo"])
    a["sapo"] -= 1
    print(a["sapo"])

def t7():     ##BADBADBADBABDBABDBABD      BAD
    if input() == 1 or 2 or 3:
        print("gay")

def t8():
    l = [1,2,3]
    l.reverse()
    print(l)

def t9():
    n = 10
    print(n%2)

def t10():
    n = 141
    print(int((n*(n+1))/2))

def t11():
    l = [1,2,3]
    print(l)
    l.append(9)
    print(l)

def t():
    l = eval("(" + input() + ")")
    print(l[-1])

t()