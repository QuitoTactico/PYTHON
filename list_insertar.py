class Node: # No cambiar esta clase
    def __init__(self, val):
        self.val = val
        self.next = None

def insertar(head: Node, valor:int, pos:int):  
    a = head
    if(pos==1):
        n = Node(valor)
        n.next = head
        return n
    while(True):
        if(head==None):
            if(pos==1):head = Node(valor)
            break
        if(pos-1==1):
            n = Node(valor)
            n.next= head.next
            head.next = n
        head = head.next
        pos = pos -1
    return a



#-------------------------- cut ---------------------------#
def largo(head: Node, i: int):
    if(head==None):return i
    return largo(head.next,i+1)
def imprimir(head : Node) -> Node:
    while(True):
        print(head.val)
        head = head.next
        if(head == None):
            break
            

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
    n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7
    l = largo(n1,0)
    print("Largo:",l)
    imprimir(n1)
    print("---")

#------------------------- cambiar -------------------------#
    res = insertar(n1,100,9)
    imprimir(res)

main()