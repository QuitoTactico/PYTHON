#There must be a single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.

def validate_battlefield(field):
    counter = {4:1,  # battleship
               3:2,  # cruisers
               2:3,  # destroyers
               1:4}  # submarines
    
    try:
        if len(field) != 10 or len(field[0]) != 10: return False # wrong dimensions
        if sum([sum(row) for row in field]) != 20: return False # wrong ships count
    except:
        return False # wrong dimensions too (smaller than expected)
    

    horizontal_validation = [(1, i) for i in [-1,0,1]]+[(-1, 1)]
    vertical_validation = [(i, 1) for i in [-1,0,1]]+[(1, -1)]
    dot_validation = [(-1,1),(1,1),(1,-1)]

    def count_ship(y, x):
        dot_count = 0

        if x+1 < 10 and field[y][x+1] == 1:                 # horizontal ship
            while x < 10 and field[y][x] == 1:
                field[y][x] = 0
                dot_count += 1
                for j, i in horizontal_validation:  # touch validation
                    if 0 <= x+i < 10 and 0 <= y+j < 10 and field[y+j][x+i] == 1: return False
                x += 1

        elif y+1 < 10 and field[y+1][x] == 1:               # vertical ship
            while y < 10 and field[y][x] == 1:
                field[y][x] = 0
                dot_count += 1
                for j, i in vertical_validation: # touch validation
                    if 0 <= x+i < 10 and 0 <= y+j < 10 and field[y+j][x+i] == 1: return False
                y += 1

        else:   # dot ship
            field[y][x] = 0
            dot_count = 1
            for j, i in vertical_validation: # touch validation
                    if 0 <= x+i < 10 and 0 <= y+j < 10 and field[y+j][x+i] == 1: return False
            
        counter[dot_count] -= 1
        return True
    

    for i, row in enumerate(field):
        for j, point in enumerate(row):
            if point == 1:
                if not count_ship(i, j): # invalid ship
                    return False
    
    
    return True if list(counter.values()) == [0]*4 else False # wrong ship count
        


# ------------------------------------------------------------------------------

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


print(validate_battlefield(battleField))


# ----------------- WTFFFFFF -------------------------

'''
from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]


    
from scipy.ndimage.measurements import label, find_objects
import numpy as np
def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]



def validate_battlefield(field):
    for i in range(10):
        for j in range(10):
            if field[i][j]:
                field[i][j] = sum(1 for x in range(max(i - 1, 0), min(i + 1, 9) + 1)
                                  for y in range(max(j - 1, 0), min(j + 1, 9) + 1) if field[x][y])
    return sum(sum(row) for row in field) == 40

    

import re
def validate_battlefield(field):
    def check(ship):
        for i in range(len(matcher)):
            ship["count"] = ship.get("count", 0) + (1 if ship["regex"].match(matcher, i) else 0)
        return ship["count"] // ship["factor"] == ship["amount"]
    ships = [
        { "name": "battleship","amount": 1,"factor": 1,"regex": re.compile("[^1]{6}.{5}[^1]1111[^1].{5}[^1]{6}")},
        { "name": "cruisers",  "amount": 2,"factor": 1,"regex": re.compile("[^1]{5}.{6}[^1]111[^1].{6}")},
        { "name": "destroyers","amount": 3,"factor": 1,"regex": re.compile("[^1]{4}.{7}[^1]11[^1].{7}[^1]{4}")},
        { "name": "submarines","amount": 4,"factor": 2,"regex": re.compile("[^1]{3}.{8}[^1]1[^1].{8}[^1]{3}")},
    ]
    joinx = lambda f: "0"*12 + ",".join("".join(map(str, l)) for l in f) + "0"*12
    matcher = joinx(field + [[0]*10] + list(zip(*field)))
    return all(map(check, ships))
'''