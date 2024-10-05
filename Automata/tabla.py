import numpy as np

lista1 = [
    238,
    240,
    127,
    132,
    86,
    220,
    149,
    162,
    118,
    139,
    87,
    128,
    126,
    212,
    142,
    243,
    262,
    255,
    140,
    82,
    265,
    149,
    105,
    255,
    260,
    168,
    90,
    194,
    242,
    250,
    260,
    90,
    126,
    82,
    172,
    121,
    114,
    215,
    172,
    125,
    230,
    162,
    172,
    175,
    126,
    235,
    171,
    156,
    155,
    148,
    118,
    126,
    129,
    229,
    135,
    161,
    127,
    195,
    216,
    149,
]

lista2 = [
    48,
    45,
    55,
    52,
    50,
    48,
    54,
    56,
    45,
    59,
    54,
    49,
    58,
    54,
    34,
    39,
    62,
    53,
    40,
    29,
    47,
    46,
    50,
    58,
    56,
    61,
    49,
    66,
    41,
    56,
    46,
    43,
    63,
    45,
    65,
    59,
    44,
    65,
    41,
    39,
    63,
    50,
    65,
    36,
    48,
    51,
    62,
    56,
    61,
    47,
    67,
    60,
    38,
    68,
    49,
    69,
    70,
    48,
    51,
    48,
]

lista3 = [
    358,
    405,
    427,
    435,
    445,
    451,
    458,
    462,
    470,
    507,
    380,
    412,
    428,
    435,
    450,
    452,
    460,
    465,
    472,
    520,
    401,
    420,
    432,
    442,
    450,
    452,
    461,
    470,
    478,
    541,
    405,
    421,
    433,
    445,
    450,
    457,
    462,
    470,
    480,
    548,
]

lista4 = list(
    map(
        int,
        "100, 100, 101, 101, 101, 102, 102, 102, 103, 103, 103, 104, 104, 107, 109, 110, 110, 110, 111, 111, 113, 113, 115, 115, 116, 116, 116, 118, 118, 120, 123, 123, 124, 125, 125, 125, 126, 126, 127, 127, 127, 127, 128, 130, 130, 130, 130, 131, 132, 133, 134, 137, 137, 137, 138, 139, 140, 140, 141, 141, 142, 143, 144, 145, 146, 146, 146, 147, 148, 148, 149, 150, 151, 152, 153, 153, 153, 153, 153, 154, 154, 155, 157, 158, 158, 158, 158, 160, 160, 160, 161, 162, 162, 163, 163, 164, 165, 165, 166, 167, 167, 168, 168, 168, 168, 169, 169, 171, 171, 171, 171, 171, 172, 174, 175, 175, 175, 176, 176, 177, 177, 177, 177, 178, 178, 179, 179, 180, 180, 181, 181, 182, 182, 184, 184, 185, 185, 186, 186, 186, 187, 187, 187, 188, 189, 189, 190, 190, 191, 191, 191, 195, 196, 196, 197, 198, 198, 199, 199, 199, 200, 200".split(
            ", "
        ),
    )
)

print(lista4)


# ----------------------------------------------

datos = lista4

# ----------------------------------------------

rango = np.ptp(datos)  # 183

# hecho con fórmula de Sturges
intervalos = int(np.ceil(np.log2(len(datos)) + 1))  # 7

amplitud = int((rango + rango * 0.1) / intervalos)


print("rango:", rango, "\n# de intervalos:", intervalos, "\namplitud:", amplitud)


# ----------------------------------------------

tablafrec = {}

i = np.min(datos)
num = 1
prom = sum(datos) / len(datos)

print(
    "i",
    "Li",
    "Ls",
    "MC",
    "F",
    "Fa",
    "Fr",
    "F%",
    "Fra",
    "Fra%",
    "|",
    "Fr*MC",
    "(MC-X)*F",
    "(MC^2)*F",
    "MC*F",
    "(MC*F)^2",
    sep="\t",
)
print("-" * 80)

while i < np.max(datos):
    inferior = i
    superior = i + amplitud - 1
    marca_clase = (inferior + superior) / 2
    datos_clase = [x for x in datos if x >= inferior and x <= superior]
    frecuencia = len(datos_clase)
    prom_clase = sum(datos_clase) / frecuencia
    if num == 1:
        frec_acum = frecuencia
    else:
        frec_acum += frecuencia
    frecuencia_relativa = frecuencia / len(datos)
    frecuencia_porcentual = frecuencia_relativa * 100
    if num == 1:
        frec_rel_acum = frecuencia_relativa
    else:
        frec_rel_acum = frec_rel_acum + frecuencia_relativa
    frec_rel_acum_porcentual = frec_rel_acum * 100

    print(
        num,
        inferior,
        superior,
        marca_clase,
        frecuencia,
        frec_acum,
        round(frecuencia_relativa, 2),
        str(round(frecuencia_porcentual, 2)) + "%",
        round(frec_rel_acum, 2),
        str(round(frec_rel_acum_porcentual, 2)) + "%",
        "|",
        round(frecuencia_relativa * marca_clase, 2),
        round((marca_clase - prom_clase) * frecuencia, 2),
        round((marca_clase**2) * frecuencia, 2),
        round(marca_clase * frecuencia, 2),
        round((marca_clase * frecuencia) ** 2, 2),
        sep="\t",
    )

    #'Fr*X*MC',
    #'(MC-X)Fa',
    #'MC^2*X*Fa',
    #'MC*Fa',
    #'(MC Fa)^2',

    i += amplitud
    num += 1
