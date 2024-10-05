# Mi favorito hasta ahora
from datetime import datetime

mes, d = {
    1: "_____Enero",
    2: "___Febrero",
    3: "_____Marzo",
    4: "_____Abril",
    5: "______Mayo",
    6: "_____Junio",
    7: "_____Julio",
    8: "____Agosto",
    9: "Septiembre",
    10: "___Octubre",
    11: "_Noviembre",
    12: "_Diciembre",
}, {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def calendario(y, m):
    d[2], s = (
        29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28
    ), datetime.strptime(f"1/{m}/{y}", "%d/%m/%Y").weekday()
    print("lun\tmar\tmie\tjue\tvie\tsab\tdom")
    for _ in range(s):
        print("\t", end="")
    for i in range(1, d[m] + 1):
        if i != 1 and s != 0:
            print(f"\t{i}", end="")
        else:
            print(i, end="")
        s += 1
        if s == 7:
            s = 0
            if i != d[m]:
                print()


modo = int(input("\nIngrese -1 para ver el calendario de todo un año. -> "))
if modo == -1:
    a = int(input("Qué año? -> "))
    for i in range(1, 13):
        print("_________________________________________" + mes[i])
        calendario(a, i)
        print("\n")
else:
    for _ in range(modo):
        s = list(map(int, input().split("/")))
        calendario(s[2], s[1])
        print("\n")
