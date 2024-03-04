class Node:
    def __init__(self, val):

        self.val = val

        self.next = None

def organizar(head:Node):
    l = []

    while(True):
        if(head==None): 
            l.sort()
            break
        l.append(head.val)
        head = head.next

    return l
def concat(head1:Node,head2:Node):
    res = head1
    while(True):
        if(head1.next == None):
            head1.next = head2
            break
        head1 = head1.next
    return res
def retornar(head:Node,l:list):
    res = head
    i = 0
    while(True):

        if(head == None):
            break
        head.val = l[i]
        head = head.next
        i = i+1
    return res

def merge(head1: Node, head2: Node) -> Node:
    if(head1==None):return head2
    if(head2 == None):return head1
    return retornar(concat(head1,head2),organizar(concat(head1,head2)))