class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def index_of(head:Node, value): 
    i = 0
    while True:
        if head is not None:
            if value == head.data:
                return i
            else:
                head = head.next
                i += 1
        else:
            return -1
