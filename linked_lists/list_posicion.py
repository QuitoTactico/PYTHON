class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def posicion(head: Node, i: int) -> int:
    if head == None: return 0
    if(i== 1):
        return head.val
    return posicion(head.next,i-1)