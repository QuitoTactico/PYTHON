class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def TamañoArbol(root: Node):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    if root.left == None:
        return TamañoArbol(root.right) + 1
    if root.right == None:
        return TamañoArbol(root.left) + 1
    return TamañoArbol(root.left) + TamañoArbol(root.right) + 1


def main():

    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)

    print(TamañoArbol(n1))


#     1
#   2   3
#  4 5 6 7


main()
