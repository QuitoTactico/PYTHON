#from preloaded import htmlize # this can help you debug your code

# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell.
import copy

def get_neighbours(cells : list[list[int]], x, y) -> int:
    count = 0
    for i in range(max(x-1,0), min(x+1,len(cells)-1) +1):
        for j in range(max(y-1,0), min(y+1,len(cells[0])-1) +1):
            if not (x == i and y == j) and cells[i][j] == 1:
                count += 1
    return count

def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]:
    game = copy.deepcopy(cells)
    
    for _ in range(generations):
        past_game = copy.deepcopy(game)

        #conway_printer(past_game)

        for i in range(len(past_game)):
            for j in range(len(past_game[i])):
                neighbours = get_neighbours(past_game, i, j)

                if past_game[i][j] == 1:
                    if neighbours != 2 and neighbours != 3:
                        game[i][j] = 0

                else: 
                    if neighbours == 3:
                        game[i][j] = 1

    return game


'''
cells = [
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
]
'''
cells = [
    [1,0,0],
    [0,1,1],
    [1,1,0]
]


def conway_printer(conway):
    for i in conway:
        for j in i:
            if j == 1:
                print("▓▓", end='')
            else:
                print("░░", end='')
        print()


conway_printer(get_generation(cells, 1))
#conway_printer(cells)
#print(htmlize(cells))