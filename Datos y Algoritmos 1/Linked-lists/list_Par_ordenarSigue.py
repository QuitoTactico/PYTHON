class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def juntar(n1: Node, n2: Node):
    if n1.next != None:
        n1.next = juntar(n1.next, n2)
        return backorder(n1, cambiar(n1, []))
    else:
        n1.next = n2
        return n1


def cambiar(head: Node, array: list) -> list:
    while head != None:
        array.append(head.val)
        head = head.next
    array.sort()
    return array


def backorder(head: Node, array: list):
    a = head
    i = 0
    while head != None:
        head.val = array[i]
        head = head.next
        i = i + 1
    return a


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
    n1 = Node(1000)
    n2 = Node(200)
    n3 = Node(300343)
    # n4 = Node(7)
    # n5 = Node(55)
    n1.next = n2
    n2.next = n3
    # n3.next = n4
    # n4.next = n5
    m1 = Node(1000000)
    m2 = Node(2500)
    m3 = Node(350)
    # m4 = Node(82315)
    # m5 = Node(6234)
    m1.next = m2
    m2.next = m3
    # m3.next = m4
    # m4.next = m5
    """n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7"""
    print(largo(n1, 0), "(Largo)")
    imprimir(n1)
    print("---")

    # ------------------------- cambiar -------------------------#
    n = juntar(n1, m1)
    imprimir(n)
    """#print(cambiar(n,[]))
    a = cambiar(n,[])
    print(a)
    #a.sort()
    #print(a, "Luego del sort()")
    imprimir(backorder(n,a))"""


main()
