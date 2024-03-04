import collections
n = collections.deque()
basuraLmao = input()
for i in map(int,input().split()):
    n.append(i)

for i in n:
    print(i)