class Node:
    def __init__(self, val=0, left=None, mid=None, right=None):
        self.val = val
        self.left = left
        self.mid = mid
        self.right = right


def Altura(root: Node = None):
    if root == None:
        return 0  # ZZZ
    if root.left == None and root.mid == None and root.right == None:
        return 1  # 000
    if root.left == None and root.mid == None:
        return Altura(root.right) + 1  # 001
    if root.left == None and root.right == None:
        return Altura(root.mid) + 1  # 010
    if root.mid == None and root.right == None:
        return Altura(root.left) + 1  # 100
    if root.left == None:
        return max(Altura(root.mid), Altura(root.right)) + 1  # 011
    if root.mid == None:
        return max(Altura(root.left), Altura(root.right)) + 1  # 101
    if root.right == None:
        return max(Altura(root.left), Altura(root.mid)) + 1  # 110
    return max(Altura(root.left), Altura(root.mid), Altura(root.right)) + 1  # 111


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    print(Altura(n1))


#     1
#   2   3
#  4 5 6 7

main()
