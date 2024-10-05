class Node:  # No cambiar esta clase
    def __init__(self, val):
        self.val = val
        self.next = None


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


# Pana, que codigazo se mandó el profe
# aprendí mucho viéndolo e hice el mío
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
    """n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7"""
    print(largo(n1, 0), "(Largo)")
    imprimir(n1)
    print("---")

    # ------------------------- cambiar -------------------------#
    n = invertir(n1)
    imprimir(n)


main()
