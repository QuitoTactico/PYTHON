import copy


def conway_printer(cells):
    for i in cells:
        for j in i:
            if j == 1:
                print("▓▓", end="")
            else:
                print("░░", end="")
        print()


def expand(cells):
    cells = (
        [[0 for _ in range(len(cells[0]))]]
        + cells
        + [[0 for _ in range(len(cells[0]))]]
    )
    cells = [[0] + item + [0] for item in cells]
    return cells


def reduce(cells):
    for _ in range(max(len(cells), len(cells[0]))):
        if sum(cells[0]) == 0:
            cells = cells[1:]
        if sum(cells[-1]) == 0:
            cells = cells[:-1]

        left, right = 0, 0
        for i in cells:
            left += i[0]
            right += i[-1]

        if left == 0:
            cells = [item[1:] for item in cells]
        if right == 0:
            cells = [item[:-1] for item in cells]
    return cells


def get_neighbours(cells: list[list[int]], x, y) -> int:
    count = 0
    for i in range(max(x - 1, 0), min(x + 1, len(cells) - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, len(cells[0]) - 1) + 1):
            if not (x == i and y == j) and cells[i][j] == 1:
                count += 1
    return count


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    game = copy.deepcopy(cells)

    for _ in range(generations):
        past_game = copy.deepcopy(game)
        past_game = expand(past_game)

        game = copy.deepcopy(past_game)

        # conway_printer(past_game)

        for i in range(len(past_game)):
            for j in range(len(past_game[i])):
                neighbours = get_neighbours(past_game, i, j)

                if past_game[i][j] == 1:
                    if neighbours != 2 and neighbours != 3:
                        game[i][j] = 0

                else:
                    if neighbours == 3:
                        game[i][j] = 1

        game = reduce(game)

    return game


"""
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
"""
cells = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]

conway_printer(get_generation(cells, 1))

"""
cells = [[0 for _ in range(len(cells[0]))]] + cells + [[0 for _ in range(len(cells[0]))]]
cells = [[0]+item+[0] for item in cells]

conway_printer(cells)
"""
"""
for i in range(3):
    cells = expand(cells)
conway_printer(cells)

cells = reduce(cells)
conway_printer(cells)
"""


# -------------------------------------- HAHHAHAHA WTF IS THIS-----------------------------


def get_neighbours2(x, y):
    return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}


def get_generation2(cells, generations):
    if not cells:
        return cells
    xm, ym, xM, yM = 0, 0, len(cells[0]) - 1, len(cells) - 1
    cells = {(x, y) for y, l in enumerate(cells) for x, c in enumerate(l) if c}
    for _ in range(generations):
        cells = {
            (x, y)
            for x in range(xm - 1, xM + 2)
            for y in range(ym - 1, yM + 2)
            if 2 < len(cells & get_neighbours(x, y)) < 4 + ((x, y) in cells)
        }
        xm, ym = min(x for x, y in cells), min(y for x, y in cells)
        xM, yM = max(x for x, y in cells), max(y for x, y in cells)
    return [
        [int((x, y) in cells) for x in range(xm, xM + 1)] for y in range(ym, yM + 1)
    ]
