def subconjuntos(s):
    subconjuntosAux(s[:-2], s[-2:])


def subconjuntosAux(a: str, b: str):
    if len(a) == 1:
        print(b)
        print(b[0])
        print(b[1])
        print("")
    else:
        print(a + b)
        print(a + b[0])
        print(a + b[1])
        print(a)

        subconjuntosAux(a[:-1], b)
        # subconjuntosAux(a[:-2]+a[-1:],b)

        s = a + b
        subconjuntos(s[1:])


subconjuntos(input())


"""
asdas
asda
asds
asd
asas
asa
ass
as
adas
ada
ads
ad
aas
aa
as
a
sdas
sda
sds
sd
sas
sa
ss
s
das
da
ds
d
as
a
s
"""
