import sys
from copy import deepcopy

def walk(maze, x, y, sum, past):
    if x == len(maze)-1 and y == len(maze[0])-1:
        return sum
    

    my_past = deepcopy(past)
    my_past[(x,y)] = True

    maze = deepcopy(maze)
    maze[x][y] = float('inf')
    
    posibles = []
    for i in range(max(x-1,0), min(x+1,len(maze)-1) +1):
        for j in range(max(y-1,0), min(y+1,len(maze[0])-1) +1):
            if not (x == i and y == j) and (x,y) not in past and (abs((x-i)+(y-j)) == 1) and maze[x][y] != float('inf'):
                new_sum = sum+abs(maze[x][y]-maze[i][j])
                posibles.append(walk(maze, i, j, new_sum, my_past))
    
    try:
        return min(posibles)
    except:
        return float('inf')

    
def path_finder(maze):
    sys.setrecursionlimit(5000)

    # pared de infinitos, jajjajaja
    matrix_maze = [[item for item in [float('inf')]+list(map(int, list(line)))+[float('inf')]] for line in maze.split()]
    matrix_maze = ([[float('inf')]*len(matrix_maze[0])])+matrix_maze+([[float('inf')]*len(matrix_maze[0])])
    
    return walk(matrix_maze, 1, 1, 0, {})


b = "\n".join([
          "010",
          "010",
          "010"
        ])

e = "\n".join([
          "700000",
          "077770",
          "077770",
          "077770",
          "077770",
          "000007"
        ])

print(path_finder(e))