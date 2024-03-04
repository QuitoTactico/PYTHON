class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#ptm que buen code se hizo este man   
def invertir(head: Node) -> Node:
    if head == None:return None
    anterior = None
    siguiente = head.next
    while (siguiente != None):
        head.next = anterior
        anterior = head
        head = siguiente
        siguiente = siguiente.next
    head.next = anterior
    return head

def largo(head: Node, i: int):
    if(head==None):return i
    return largo(head.next,i+1)
def imprimir(head : Node) -> None:
    while(head != None):
        print(head.val)
        head = head.next
def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    '''n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7'''
    print(largo(n1,0),"(Largo)")
    imprimir(n1)
    print("---")

#------------------------- cambiar -------------------------#
    n = invertir(n1)
    imprimir(n)
main()