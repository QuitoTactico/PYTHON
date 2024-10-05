class Node:  # No cambiar esta clase
    def __init__(self, val):
        self.val = val
        self.next = None


def sumar(head1: Node, head2: Node):
    h1 = invertir(head1)
    h2 = invertir(head2)
    """sum = h1
    while(h2.next!=None):
        sumtemp = int(h1.val)+int(h2.val)
        if(sumtemp >= 10):
            if(h1.next == None):
                #h1.val = sumtemp-10
                h1.val = 0
                h1.next = Node(1)
            if(h1.next != None):
                #h1.val = sumtemp-10
                h1.val = 0
                (h1.next).val = (h1.next).val+1
        if(sumtemp < 10):
            h1.val = sumtemp

        if(h1.next == None):
            h1.next = h2.next
            #break
        h1= h1.next
        h2= h2.next"""
    h1 = f(h1, h2)
    return invertir(h1)


def f(h1: Node, h2: Node):
    if h1 == None:
        return h2
    if h2 == None:
        return h1
    # print(h1.val,"-")
    # print(h2.val,"-")
    temp = int(h1.val) + int(h2.val)
    # print(temp,"--")
    if temp < 10:
        h1.val = temp
    if temp >= 10:
        h1.val = temp - 10
        if h1.next != None:
            (h1.next).val = (h1.next).val + 1
        if h1.next == None:
            h1.next = Node(1)
    h1.next = f(h1.next, h2.next)
    return h1


def invertir(head: Node):
    if head == None:
        return None
    temp = None
    # node es node, obvio, head = head
    nexto = head.next
    while True:
        if nexto == None:
            head.next = temp
            return head
        head.next = temp
        temp = head
        head = nexto
        nexto = nexto.next


# ------------------------ cut -----------------------------#


def largo(head: Node, i: int):
    if head == None:
        return i
    return largo(head.next, i + 1)


def imprimir(head: Node) -> None:
    while head != None:
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
    m1 = Node(1)
    m2 = Node(2)
    m3 = Node(3)
    m4 = Node(4)
    m5 = Node(5)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    m4.next = m5
    """n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7"""
    print(largo(n1, 0), "(Largo)")
    imprimir(n1)
    print("---")

    # ------------------------- cambiar -------------------------#
    n = sumar(n1, m1)
    imprimir(n)
    # imprimir(invertir(n1))


main()
