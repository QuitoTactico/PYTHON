dayres = {
    0: "sabado",
    1: "domingo",
    2: "lunes",
    3: "martes",
    4: "miércoles",
    5: "jueves",
    6: "viernes",
}
mes = {
    "enero": 13,
    "febrero": 14,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}


def zellergod(d, m, y):
    m = mes[m]
    if m > 12:
        y -= 1
    res = (d + ((13 * (m + 1)) // 5) + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return dayres[res]


for _ in range(int(input())):
    fecha = input().split("-")
    print(zellergod(int(fecha[0]), fecha[1], int(fecha[2])))
