from heapq import heappop, heappush
from math import inf


def path_finder(area):
    grid = [list(map(int, line)) for line in area.split("\n")]
    size = len(grid)
    distances = [[inf] * size for _ in range(size)]
    heap = [(0, 0, 0)]
    while True:
        distance, x, y = heappop(heap)
        if x == y == size - 1:
            return distance
        if distances[y][x] != inf:
            continue
        distances[y][x] = distance
        for xx, yy in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)):
            if 0 <= xx < size and 0 <= yy < size and distances[yy][xx] == inf:
                new_distance = distance + abs(grid[y][x] - grid[yy][xx])
                heappush(heap, (new_distance, xx, yy))
