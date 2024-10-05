from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vistaSup(root: Node):
    if root == None:
        return ""
    vista = deque()
    arbol = root
    while root != None:
        vista.append(root.val)
        root = root.right
    root = arbol.left
    while root != None:
        vista.appendleft(root.val)
        root = root.left

    res = str(list(vista)).replace(",", "")
    res = res[1:-1]
    return list(vista)
    # BRO, SE SUPONÍA QUE ERA RETORNAR UN STRING CON LOS NÚMEROS
    # SEPARADOS POR ESPACIOS. NO UNA LISTA. Pero bueno.


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    print(vistaSup(n1))


#     1
#   2   3
#  4 5 6 7

main()
