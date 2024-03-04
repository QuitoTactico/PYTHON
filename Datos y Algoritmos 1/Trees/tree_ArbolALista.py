
from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ArbolALista(root: Node) -> None:
    if root == None : return None
    
    arbol = Node("aux")
    arbolaux = arbol
    for i in dequeArbol(root):
        arbol.right = Node(i)
        arbol = arbol.right

    root = arbolaux.right
    return root  ###

def dequeArbol(root : Node):
    res = deque([root.val])
    if root == None : return None

    if root.left == None and root.right == None: return res

    if root.left == None: 
        res.extend(dequeArbol(root.right))
        return res
    if root.right == None: 
        res.extend(dequeArbol(root.left))
        return res

    res.extend(dequeArbol(root.left))
    res.extend(dequeArbol(root.right))
    return res

def imprimir(head : Node) -> None:
    while(head != None):
        print(head.val)
        head = head.right

def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2,n4,n5)
    n3 = Node(3,n6,n7)
    
    n1 = Node(1,n2,n3)
    imprimir(ArbolALista(n1))

#     1
#   2   3
#  4 5 6 7

main()