import sys


def walk(maze, x, y):
    if maze[x][y] == "W":
        return False

    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return True

    maze[x][y] = "W"

    possible = False
    for i in range(max(x - 1, 0), min(x + 1, len(maze) - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, len(maze[0]) - 1) + 1):
            if (
                not (x == i and y == j)
                and maze[i][j] != "W"
                and (abs((x - i) + (y - j)) == 1)
            ):
                # possible = possible or walk(maze, i, j)
                # if possible:
                if walk(maze, i, j):
                    return True
    return False


def path_finder(maze):
    sys.setrecursionlimit(5000)
    matrix_maze = [[item for item in list(line)] for line in maze.split()]
    return walk(matrix_maze, 0, 0)


maze = "\n".join([".W.", ".W.", "..."])

print(path_finder(maze))
