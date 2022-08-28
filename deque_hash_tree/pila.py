import collections

n = int(input())
#nums = list(map(int,input().split(" ")))
pila = collections.deque(list(map(int,input().split(" "))))
for i in range(n):
    print(pila.pop())


#print(pila)h