import collections
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def invertir(head: Node) -> Node:
    if(head==None):return None
    pila = collections.deque()
    while(head!=None):
        pila.appendleft(head)
        head = head.next
    for i in range(1,len(pila)):
        pila[i-1].next = pila[i]
    
    pila[-1].next = None
    return pila[0]

def imprimir(head:Node):
    while(head!=None):
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
    print("---")

#------------------------- cambiar -------------------------#
    n = invertir(n1)
    imprimir(n)

main()