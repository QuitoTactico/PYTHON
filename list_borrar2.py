class Node:
    def _init_(self, val):
        self.val = val
        self.next = None

def borrar(head: Node, pos:int):
    if(head == None):
        return 0
    elif(pos == 1):
        new = head.next
        head.next = head
        head.next = new.next
        return head
    else:
        previo = head
        while previo.next.val != pos:
            if previo.next == None:
                return head
            else:
                before = previo
                previo = previo.next
            new =  previo.next
            before.next = new
            return head