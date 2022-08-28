class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def invertir(head: Node) -> Node:
  if head == None:
    return None
  anterior = None
  actual = head
  siguiente = head.next
  while (siguiente != None):
    actual.next = anterior
    anterior = actual
    actual = siguiente
    siguiente = siguiente.next
  actual.next = anterior
  return actual
  
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
 imprimir(n1)
 print(":)")
 inv = invertir(n1)
 imprimir(inv)
 
main()
