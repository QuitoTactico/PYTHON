class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ArbolesIguales(root1: Node, root2: Node):
    if root1 == None and root2 == None:
        return True
    if root1.val == root2.val:
        return ArbolesIguales(root1.left, root2.left) and ArbolesIguales(
            root1.right, root2.right
        )
    return False


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    n8 = Node(1, n2, n2)
    print(ArbolesIguales(n1, n8))


#     1
#   2   3
#  4 5 6 7

main()
