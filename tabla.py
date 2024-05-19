import numpy as np

lista1 = [
    238
    ,240
    ,127
    ,132
    ,86
    ,220
    ,149
    ,162
    ,118
    ,139
    ,87
    ,128
    ,126
    ,212
    ,142
    ,243
    ,262
    ,255
    ,140
    ,82
    ,265
    ,149
    ,105
    ,255
    ,260
    ,168
    ,90
    ,194
    ,242
    ,250
    ,260
    ,90
    ,126
    ,82
    ,172
    ,121
    ,114
    ,215
    ,172
    ,125
    ,230
    ,162
    ,172
    ,175
    ,126
    ,235
    ,171
    ,156
    ,155
    ,148
    ,118
    ,126
    ,129
    ,229
    ,135
    ,161
    ,127
    ,195
    ,216
    ,149
]

lista2 = [
    48
    ,45
    ,55
    ,52
    ,50
    ,48
    ,54
    ,56
    ,45
    ,59
    ,54
    ,49
    ,58
    ,54
    ,34
    ,39
    ,62
    ,53
    ,40
    ,29
    ,47
    ,46
    ,50
    ,58
    ,56
    ,61
    ,49
    ,66
    ,41
    ,56
    ,46
    ,43
    ,63
    ,45
    ,65
    ,59
    ,44
    ,65
    ,41
    ,39
    ,63
    ,50
    ,65
    ,36
    ,48
    ,51
    ,62
    ,56
    ,61
    ,47
    ,67
    ,60
    ,38
    ,68
    ,49
    ,69
    ,70
    ,48
    ,51
    ,48
]

lista3 = [
    358
    ,405
    ,427
    ,435
    ,445
    ,451
    ,458
    ,462
    ,470
    ,507
    ,380
    ,412
    ,428
    ,435
    ,450
    ,452
    ,460
    ,465
    ,472
    ,520
    ,401
    ,420
    ,432
    ,442
    ,450
    ,452
    ,461
    ,470
    ,478
    ,541
    ,405
    ,421
    ,433
    ,445
    ,450
    ,457
    ,462
    ,470
    ,480
    ,548
]


#----------------------------------------------

datos = lista3

#----------------------------------------------

rango = np.ptp(datos)                              # 183

# hecho con fórmula de Sturges
intervalos = int(np.ceil(np.log2(len(datos)) + 1)) # 7

amplitud = int((rango + rango*0.1) / intervalos )


print('rango:', rango, '\n# de intervalos:', intervalos, '\namplitud:', amplitud)


#----------------------------------------------

tablafrec = {}

i = np.min(datos)
num = 1
print('i','Li','Ls','MC','F','Fa','Fr','F%','Fra','Fra%', sep='\t')
print('-'*80)
while i < np.max(datos):
    inferior = i
    superior = i + amplitud - 1
    marca_clase = (inferior + superior) / 2
    frecuencia = len([x for x in datos if x >= inferior and x <= superior])
    if num == 1:
        frec_acum = frecuencia
    else:
        frec_acum += frecuencia
    frecuencia_relativa = frecuencia / len(datos)
    frecuencia_porcentual = frecuencia_relativa * 100
    if num == 1:
        frec_rel_acum = frecuencia_relativa
    else:
        frec_rel_acum = frec_rel_acum+frecuencia_relativa
    frec_rel_acum_porcentual = frec_rel_acum * 100

    print(num, inferior, superior, marca_clase, frecuencia, frec_acum, round(frecuencia_relativa,2), str(round(frecuencia_porcentual,2))+'%', round(frec_rel_acum,2), str(round(frec_rel_acum_porcentual,2))+'%', sep='\t')
    i += amplitud
    num += 1



