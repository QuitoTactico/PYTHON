class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def borrar(head: Node, pos):
    if head == None:
        return 0
    while head.next != None:
        if pos == 1:
            a = head.next
            head.next = a.next
    head.next = borrar(head.next, pos - 1)
    return head
