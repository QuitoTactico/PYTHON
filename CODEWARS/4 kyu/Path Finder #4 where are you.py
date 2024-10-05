me = {"x": 0, "y": 0, "dir": 0}


def move(moves):
    global me
    if me["dir"] == 0:
        me["y"] -= moves
    if me["dir"] == 1:
        me["x"] += moves
    if me["dir"] == 2:
        me["y"] += moves
    if me["dir"] == 3:
        me["x"] -= moves


def i_am_here(path: str):
    global me

    moves = 0
    for i, command in enumerate(path):
        if command.isdigit():
            moves = moves * 10 + int(command)
            if i == len(path) - 1:
                move(moves)
                moves = 0
        else:
            move(moves)
            moves = 0
            if command == "r":
                me["dir"] = (me["dir"] + 1) % 4
            if command == "l":
                me["dir"] = (me["dir"] - 1) % 4
            if command in ["R", "L"]:
                me["dir"] = (me["dir"] + 2) % 4

    return [me["y"], me["x"]]
