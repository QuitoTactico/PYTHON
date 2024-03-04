class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def mezclar(head1:Node,head2:Node) -> Node:
    res = head1
    while(True):
        if(head1.next == None):
            head1.next = head2
            return res
        head1 = head1.next
def toList(head:Node) -> list:
    l = []
    while(True):
        if(head==None): 
            l.sort()
            return l
        l.append(head.val)
        head = head.next
def toNode(head:Node,l:list) -> Node:
    res = head
    i = 0
    while(True):
        if(head == None):
            return res
        head.val = l[i]
        head = head.next
        i = i+1

def merge(head1, head2):
    m = mezclar(head1,head2)  #
    l = toList(m)       #
    n = toNode(m,l)
    return n

#------------------------ cut -----------------------------#

def largo(head: Node, i: int):
    if(head==None):return i
    return largo(head.next,i+1)
def imprimir(head : Node) -> None:
    while(head != None):
        print(head.val)
        head = head.next
def main():
    n1 = Node(1000)
    n2 = Node(200)
    n3 = Node(300343)
    n1.next = n2
    n2.next = n3
    
    m1 = Node(100)
    m2 = Node(2500)
    m3 = Node(350)
    m1.next = m2
    m2.next = m3
    
    #m = mezclar(n1,m1)  #
    #l = toList(m)       #
    #n = toNode(m,l)     #
    #return n

    imprimir(merge(n1,m1))
main()

