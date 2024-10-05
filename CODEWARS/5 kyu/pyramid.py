def interior(n):
    s = ""
    for i in range(n * 2):
        s = "|" + s if (i - 1) % 3 == 0 else "_" + s
    return "__" if n == 1 else "__:_" if n == 2 else s


def subiendo(n):
    s = " ."
    for i in range(n):
        s = s + " \\" if i == 1 and n % 2 == 1 else s + "´\\"
    return s + "/"


def bajando(n, total):
    s = "\\/"
    for i in range(total - n - 1):
        s = (
            "\\ " + s
            if n % 2 == 1 and total // 2 == n and i == total - n - 2
            else "\\´" + s
        )
    return s


def espacio_upperleft(n, total):
    return "".join([" " * ((total - n - 1) * 3)])


def espacio_right(n, total):
    return "".join([" " * (total * 2 - n - 1)])


def espacio_downleft(n, total):
    return "".join([" " * (n - total // 2)])


def draw_pyramid(n):

    piramide_subiendo = [
        espacio_upperleft(i, n)
        + subiendo(i)
        + interior(i)
        + "\\"
        + espacio_right(i, n)
        + "|"
        for i in range(n)
    ]
    piramide_bajando = [
        espacio_downleft(i, n * 2)
        + bajando(i, n * 2)
        + interior(i)
        + "\\"
        + espacio_right(i, n)
        + "|"
        for i in range(n, n * 2)
    ]

    return "\n".join(piramide_subiendo + piramide_bajando)


# print(draw_pyramid(3))


def NOVA_ASCII():
    print("mmmmm                                                             mmmmm ")
    print(
        'MM        `7MN.   `7MF`  .g8""8q.   `7MMF`   `7MF`      db           MM          ____    __      _______ .__   __.  _______ '
    )
    print(
        "MM          MMN.    M  .dP'    `YM.   `MA     ,V       ;MM:          MM         |___ \  /_ |    |   ____||  \ |  | |   ____|"
    )
    print(
        "MM          M YMb   M  dM'      `MM    VM:   ,V       ,V^MM.         MM           __) |  | |    |  |__   |   \|  | |  |__   "
    )
    print(
        "MM          M  `MN. M  MM        MM     MM.  M'      ,M  `MM         MM          |__ <   | |    |   __|  |  . `  | |   __|  "
    )
    print(
        "MM          M   `MM.M  MM.      ,MP     `MM A'       AbmmmqMA        MM          ___) |  | |    |  |____ |  |\   | |  |____ "
    )
    print(
        "MM          M     YMM  `Mb.    ,dP'      :MM;       A'     VML       MM         |____/   |_|    |_______||__| \__| |_______|"
    )
    print("MM        .JML.    YM    `'bmmd`'         VF      .AMA.   .AMMA.     MM ")
    print("MM                                                                   MM ")
    print("MMmmm                                                             mmmMM ")

    input()


"""
 ____    __      _______ .__   __.  _______ 
|___ \  /_ |    |   ____||  \ |  | |   ____|
  __) |  | |    |  |__   |   \|  | |  |__   
 |__ <   | |    |   __|  |  . `  | |   __|  
 ___) |  | |    |  |____ |  |\   | |  |____ 
|____/   |_|    |_______||__| \__| |_______|
"""
