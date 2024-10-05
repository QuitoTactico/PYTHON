class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def InsertarBST(root: Node, val):
    if root == None:
        return Node(val)
    arbol = root
    while True:
        if val < root.val:
            if root.left == None:
                root.left = Node(val)
                break
            else:
                root = root.left
                continue
        if root.val < val:
            if root.right == None:
                root.right = Node(val)
                break
            else:
                root = root.right
                continue
    return arbol
