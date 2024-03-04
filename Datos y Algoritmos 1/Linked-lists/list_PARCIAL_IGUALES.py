class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def iguales(l1:Node,l2:Node):
    if(l1==None and l2==None):return True
    if(l1==None or l2==None):return False
    if(l1.next == None and l2.next == None):
        if(l1.val != l2.val):return False
        return True
    elif((l1 == None and l2 != None)or(l1 != None and l2 == None)):return False
    if(l1.val==l2.val):return iguales(l1.next,l2.next)
    return False
#------------------------ cut -----------------------------#

def largo(head: Node, i: int):
    if(head==None):return i
    return largo(head.next,i+1)
def imprimir(head : Node) -> None:
    while(head != None):
        print(head.val)
        head = head.next
def main():
    head1 = Node(1)
    head2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    head1.next = head2
    head2.next = n3
    n3.next = n4
    n4.next = n5
    m1 = Node(1)
    m2 = Node(2)
    m3 = Node(3)
    m4 = Node(4)
    m5 = Node(5)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    m4.next = m5
    '''n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7'''
    print(largo(head1,0),"(Largo)")
    imprimir(head1)
    print("---")

#------------------------- cambiar -------------------------#
    n = iguales(head1,m1)
    #imprimir(n)
    print(n)
main()