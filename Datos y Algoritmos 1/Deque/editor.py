from collections import deque


def menu(i):
    historial = deque()
    s = deque()

    for _ in range(i):
        n = list(map(str, input().split(" ")))
        n1 = int(n[0])
        if n1 == 1:
            historial.append(list(s))
            s.extend(list(n[1]))
        if n1 == 2:
            historial.append(list(s))
            for _ in range(int(n[1])):
                s.pop()
        if n1 == 3:
            print(s[int(n[1]) - 1])
        if n1 == 4:
            s = deque(historial.pop())
        if n1 == 5:
            print(s)


menu(int(input()))
