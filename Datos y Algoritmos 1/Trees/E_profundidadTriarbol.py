class Node:
    def __init__(self, val=0, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def depth(root:Node = None):
    if root == None :                                                    return 0   #ZZZ
    if root.left == None and root.middle == None and root.right == None: return 1   #000
    if root.left == None and root.middle == None :    return depth(root.right) +1   #001
    if root.left == None and root.right == None :    return depth(root.middle) +1   #010
    if root.middle == None and root.right == None :    return depth(root.left) +1   #100
    if root.left == None:     return max(depth(root.middle),depth(root.right)) +1   #011 
    if root.middle == None:     return max(depth(root.left),depth(root.right)) +1   #101
    if root.right == None:     return max(depth(root.left),depth(root.middle)) +1   #110
    return          max(depth(root.left),depth(root.middle),depth(root.right)) +1   #111


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2,n4,n5)
    n3 = Node(3,n6,n7)
    
    n1 = Node(1,n2,n3)
    print(depth(n1))

#     1 
#   2   3
#  4 5 6 7

main()