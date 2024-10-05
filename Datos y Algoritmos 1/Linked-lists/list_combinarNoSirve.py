class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge(n1: Node, n2: Node):
    if n1.next != None:
        n1.next = merge(n1.next, n2)
        lista = cambiar(n1, [])
        return backorder(lista, n1, 0)
    else:
        n1.next = n2
        return n1


def cambiar(head: Node, array: list):
    while head != None:
        array.append(head.val)
        head = head.next
    array.sort()
    return array


def backorder(array: list, n1: Node, i: int):
    if i < len(array):
        new = Node(array[i])
        siguiente = new
        siguiente.next = array
        return siguiente
    backorder(array, n1, i - 1)


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
    """n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7"""
    m1 = Node(1)
    m2 = Node(2)
    m3 = Node(3)
    m4 = Node(4)
    m5 = Node(5)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    m4.next = m5
    imprimir(n1)
    print("---")

    # ------------------------- cambiar -------------------------#
    n = merge(n1, m1)
    imprimir(n)


main()
