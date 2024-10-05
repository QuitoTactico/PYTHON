class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BuscarBST(root: Node, val):
    return "YES" if BuscarAUX(root, val) == True else "NO"


def BuscarAUX(root: Node, val):
    if root == None:
        return False
    if root.val == val:
        return True
    if root.left == None and root.right == None:
        return False
    if root.left == None:
        return BuscarAUX(root.right, val)
    if root.right == None:
        return BuscarAUX(root.left, val)
    return BuscarAUX(root.left, val) or BuscarAUX(root.right, val)


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    print(BuscarBST(n1, 7))


#     1
#   2   3
#  4 5 6 7

main()
