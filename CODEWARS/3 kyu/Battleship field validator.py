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

    '''
    def count_ship(x, y):
        dot_count = 0
        if x+1 field[y][x+1] == 1: # horizontal ship
            
        elif field[y+1][x] == 1: # vertical ship

    for i, row in enumerate(field):
        for j, point in enumerate(row):
            if point == 1:
                if not count_ship(): # invalid ship
                    return False
    '''
    
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