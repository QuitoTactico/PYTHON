from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


input_basura_estopaque = input()
n = deque(map(int, input().split(" ")))
# print(n)    ###

arbol = Node(n.popleft())

print(0)
# print(n)    ###
for i in n:
    nuevo = Node(i)
    actual = arbol
    comparaciones = 0
    while True:
        comparaciones = comparaciones + 1
        if nuevo.val < actual.val:
            if actual.left == None:
                actual.left = nuevo
                print(comparaciones)
                break
            else:
                actual = actual.left
                continue
        if nuevo.val > actual.val:
            if actual.right == None:
                actual.right = nuevo
                print(comparaciones)
                break
            else:
                actual = actual.right
                continue
