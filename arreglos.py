def chequeoarreglo(a: list):
    b = False
    if((len(a) >= 1) and (a[0]==a[-1])):
        b = True
    return b