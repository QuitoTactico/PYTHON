from heapq import *


def path_finder(maze):
    lst = [[int(c) for c in row] for row in maze.split("\n")]
    X, Y = len(lst), len(lst[0])
    end = (X - 1, Y - 1)
    q, seens = [(0, end == (0, 0), 0, 0)], {(0, 0): 0}
    while q and not q[0][1]:
        c, _, x, y = heappop(q)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new = a, b = x + dx, y + dy
            if 0 <= a < X and 0 <= b < Y:
                dc = abs(lst[a][b] - lst[x][y])
                if seens.get(new, float("inf")) > c + dc:
                    heappush(q, (c + dc, new == end, a, b))
                    seens[new] = c + dc
    return q[0][0]
