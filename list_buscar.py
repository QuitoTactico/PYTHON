class Node:
    def _init_(self, val):
        self.val = val
        self.next = None

def buscar(head: Node, k:int) -> int:
    if(head == None):
        return -1
    if(head.val == k):
        return 0
    c = buscar(head.next,k)
    if c!= -1: c=c+1
    return c