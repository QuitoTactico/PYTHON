import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None     
a,b = input() , collections.deque(map(int,input().split(" ")))
arbol = Node(b.popleft())
print(int("0"))
for i in b:
    nuevo = Node(i)
    c = 0
    actual = arbol
    msnmsnms = True
    while(msnmsnms):
        c = c +  1
        if nuevo.val < actual.val:
            if actual.l == None: 
                actual.l = nuevo
                print(c)
                break
            actual = actual.l
            continue
        if actual.r == None:
            actual.r = nuevo
            print(c)
            break
        actual = actual.r
        continue
