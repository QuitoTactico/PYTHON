class Node:
    def _init_(self, val: int):
        self.val = val
        self.next = None


def maximo(head: Node) -> int:
    if head == None:
        return 0
    return max(maximo(head.next), head.val)
