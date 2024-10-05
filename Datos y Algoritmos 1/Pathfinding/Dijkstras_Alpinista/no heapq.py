def path_finder(maze):
    grid = maze.splitlines()
    end = h, w = len(grid) - 1, len(grid[0]) - 1
    bag, seen = {(0, 0): 0}, set()
    while bag:
        x, y = min(bag, key=bag.get)
        rounds = bag.pop((x, y))
        seen.add((x, y))
        if (x, y) == end:
            return rounds
        for u, v in (-1, 0), (0, 1), (1, 0), (0, -1):
            m, n = x + u, y + v
            if (m, n) in seen or not (0 <= m <= h and 0 <= n <= w):
                continue
            new_rounds = rounds + abs(int(grid[x][y]) - int(grid[m][n]))
            if new_rounds < bag.get((m, n), float("inf")):
                bag[m, n] = new_rounds
