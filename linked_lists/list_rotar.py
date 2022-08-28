class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
def rotar(head: Node, k):
    primero = head
    anterior = None
    if head == None:
        return None
    else:
        for i in range(k):
            while(head.next != None):
                anterior = head
                head = head.next
            if head.next == None:
                head.next = primero
                anterior.next = None
                return head