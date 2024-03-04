class Node: # No cambiar esta clase
    def __init__(self, val):
        self.val = val
        self.next = None

def insertar(head: Node, valor:int, pos:int):  
    if(head==None): 
        if(pos==1):
            nuevoUwUXD = Node(valor)
            nuevoUwUXD.next = head
            return nuevoUwUXD
        return head
    if(pos==1):
        nuevoUwUXD = Node(valor)
        nuevoUwUXD.next = head
        return nuevoUwUXD
    else:    
        head.next = insertar(head.next, valor, pos-1)
    return head



#-------------------------- cut ---------------------------#
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
    n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7
    l = largo(n1,0)
    print("Largo:",l)
    index = 0
    if(l%2==0):index = l/2
    else:index = (l+1)/2
    print("Index:",int(index))
    imprimir(n1)
    print("---")

#------------------------- cambiar -------------------------#
    res = insertar(n1,100,8)
    imprimir(res)
 
main()