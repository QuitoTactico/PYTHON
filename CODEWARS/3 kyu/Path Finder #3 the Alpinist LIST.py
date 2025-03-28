import sys
from copy import deepcopy


def walk(maze, x, y, sum, past):
    global min_llegada

    if sum >= min_llegada:
        return float("inf")

    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        min_llegada = min(sum, min_llegada)
        return sum

    past = deepcopy(past)
    past[f"{x} {y}"] = True

    posibles = []
    for i in range(max(x - 1, 0), min(x + 1, len(maze) - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, len(maze[0]) - 1) + 1):
            if (abs((x - i) + (y - j)) == 1) and f"{i} {j}" not in past:
                new_sum = sum + abs(maze[x][y] - maze[i][j])
                if new_sum < min_llegada:
                    caminata = walk(maze, i, j, new_sum, past)
                    if caminata != float("inf"):
                        posibles.append(caminata)

    try:
        return min(posibles)
    except:
        return float("inf")


def path_finder(maze):
    global min_llegada
    # min_llegada = float('inf')
    # min_llegada = 5

    sys.setrecursionlimit(5000)

    matrix_maze_beta = [
        [item for item in list(map(int, list(line)))] for line in maze.split()
    ]
    # matrix_maze = matrix_maze_beta
    matrix_maze = []
    for i, item in enumerate(matrix_maze_beta):
        if i == len(matrix_maze_beta) - 1 or item != matrix_maze_beta[i + 1]:
            matrix_maze.append(item)
    """
    for i, item in enumerate(matrix_maze_beta):
        if i==len(matrix_maze_beta)-1 or item!=matrix_maze_beta[i+1]:
            matrix_maze.append(item)
    """
    # min_llegada = sum(matrix_maze[-1]) + sum(item[0] for item in matrix_maze) # L
    counter = 1
    L_list = matrix_maze[-1] + [item[0] for item in matrix_maze]
    last = L_list[0]
    for i in L_list[1:]:
        counter = counter + abs(i - last)
        last = i

    min_llegada = counter

    # return(counter)
    return walk(matrix_maze, 0, 0, 0, {})


b = "\n".join(["010", "010", "010"])

a = "\n".join(["7000", "0777", "0777", "0777", "0777", "0000"])

e = "\n".join(["700000", "077770", "077770", "077770", "077770", "000007"])

f = "\n".join(["777000", "007000", "007000", "007000", "007000", "007777"])

g = "\n".join(["000000", "000000", "000000", "000010", "000109", "001010"])

h = "99321659285\n82274152378\n95311209346\n11818079185\n50926731149\n06934617619\n05718311124\n91803296898\n42959100694\n70004528365\n76632198148"

print(path_finder(h))
