class Node: # No cambiar esta clase
    def __init__(self, val):
        self.val = val
        self.next = None

def final(head):
    while(True):
        if(head.next == None):return head
        head = head.next
def sinfin(head):
    a = head
    while(True):
        if(head.next.next == None):
            head.next = None
            break
        head =head.next
    return a

'''def hacetodo(inicio:Node,loquequeda:Node):
    a = inicio
    while(True):
        if(inicio.next==None):
            inicio.next = final(loquequeda)
            loquequeda = sinfin(loquequeda)
            break
        inicio = inicio.next
    if(loquequeda==None):
        return a
    else: return hacetodo(a,loquequeda)'''
#------------------------ cut -----------------------------#

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
    a = final(n1)
    a.next = sinfin(n1)
    imprimir(a)
    
main()