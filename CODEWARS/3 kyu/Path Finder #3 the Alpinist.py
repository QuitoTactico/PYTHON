import sys
from copy import deepcopy

min_llegada = float('inf')

def walk(maze, x, y, sum, past):
    global min_llegada

    if x == len(maze)-1 and y == len(maze[0])-1:
        min_llegada = min(sum, min_llegada)
        return sum
    
    if sum >= min_llegada:
        return float('inf')

    #maze = deepcopy(maze)
    #maze[x][y] = '.'
    past = deepcopy(past)
    past[f'{x} {y}'] = True
    
    posibles = []
    for i in range(max(x-1,0), min(x+1,len(maze)-1) +1):
        for j in range(max(y-1,0), min(y+1,len(maze[0])-1) +1):
            if (abs((x-i)+(y-j)) == 1) and f'{i} {j}' not in past:
                new_sum = sum+abs(maze[x][y]-maze[i][j])
                posibles.append(walk(maze, i, j, new_sum, past))
    
    try:
        return min(posibles)
    except:
        return float('inf')

    
def path_finder(maze):
    sys.setrecursionlimit(5000)

    # pared de infinitos, jajjajaja
    #matrix_maze = [[item for item in [float('inf')]+list(map(int, list(line)))+[float('inf')]] for line in maze.split()]
    #matrix_maze = ([[float('inf')]*len(matrix_maze[0])])+matrix_maze+([[float('inf')]*len(matrix_maze[0])])
    matrix_maze = [[item for item in list(map(int, list(line)))] for line in maze.split()]
    
    return walk(matrix_maze, 0, 0, 0, {})


b = "\n".join([
          "010",
          "010",
          "010"
        ])

a = "\n".join([
          "7000",
          "0777",
          "0777",
          "0777",
          "0777",
          "0000"
        ])

e = "\n".join([
          "700000",
          "077770",
          "077770",
          "077770",
          "077770",
          "000007"
        ])

f = "\n".join([
          "777000",
          "007000",
          "007000",
          "007000",
          "007000",
          "007777"
        ])

print(path_finder(e))