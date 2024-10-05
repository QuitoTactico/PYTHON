from collections import deque


def path_finder(maze: str) -> int | bool:
    table = list(map(list, maze.split("\n")))
    max_len = len(table[0]) - 1
    if max_len == 0:
        return 0

    stack = deque()
    stack.append([0, 0])
    history = {(0, 0): None}
    result = False

    while stack:
        element = stack.pop()

        x = element[1]
        y = element[0]

        if element == [max_len, max_len]:
            result = True
            break

        if table[y][x] == "x":
            continue

        if (
            max_len >= y
            and max_len >= x + 1
            and table[y][x + 1] == "."
            and table[y][x + 1] != "x"
        ):
            stack.appendleft([y, x + 1])
            history[y, x + 1] = [y, x]

        if (
            max_len >= y + 1
            and max_len >= x
            and table[y + 1][x] == "."
            and table[y + 1][x] != "x"
        ):
            stack.appendleft([y + 1, x])
            history[y + 1, x] = [y, x]

        if y - 1 >= 0 and x >= 0 and table[y - 1][x] == "." and table[y - 1][x] != "x":
            stack.appendleft([y - 1, x])
            history[y - 1, x] = [y, x]

        if y >= 0 and x - 1 >= 0 and table[y][x - 1] == "." and table[y][x - 1] != "x":
            stack.appendleft([y, x - 1])
            history[y, x - 1] = [y, x]

        table[y][x] = "x"

    if not result:
        return False

    current = history[max_len, max_len]
    path = [current]

    while current != [0, 0]:
        if current is None:
            break

        x = current[1]
        y = current[0]

        current = history[y, x]
        path.append(current)

    return len(path)
