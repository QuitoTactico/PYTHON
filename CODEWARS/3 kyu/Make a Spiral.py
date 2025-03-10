# Make a spiral

# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

# ============ FORMATTING =============

def printer(m):
    for n in m.values():
        for i in n.values():
            print(i, end=' ')
        print()
    print()

def returner(m):
    return [list(n.values()) for n in m.values()]

# ============= CONSTRUCTING =============

def spiral_creation(m, size):
    border = 0

    dot_skip_done = False

    while border < size/2:

        # dot between left start and next top start
        if dot_skip_done: # we won't do this the first time
            m[border][border-1] = 1
        else: 
            dot_skip_done = True

        # top, right and bottom
        for i in range(border, size-border):
            m[border][i] = 1 # top
            m[i][size-border-1] = 1 # right
            m[size-border-1][size-i-1] = 1 # bottom
        
        # left
        for i in range(border+2, size-border):
            m[i][border] = 1 # left
        
        border += 2
    
    m = spiral_dot_cleaning(m, size)

    return m


def spiral_dot_cleaning(m, size):
    if (size%4) == 2:
        m[size//2][(size//2)-1] = 0

    return m


def spiralize(size):
    m = {j : {i:0 for i in range(size)} for j in range(size)}

    m = spiral_creation(m, size)

    printer(m)
    return returner(m)

print(spiralize(5))



# CLEVER THAN ME:

import numpy as np

def spiralize2(size):
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1,1],[0,1]]
    sp = np.zeros((size, size))
    sp[0, :] = 1
    sp[:, -1] = 1
    sp[-1, :] = 1
    sp[2:, :-2] = np.array(spiralize(size-2))[::-1,::-1]
    return sp.tolist()