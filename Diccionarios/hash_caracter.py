def caracter(cadena):
    cadena = str(cadena).replace(" ", "")
    print(cadena)
    if cadena == None: return ""
    hash = {}
    for i in cadena:
        hash[i] = 0
    for i in cadena:
        hash[i] = hash[i]+1
        if hash[i] == 2: return i
    return ""

print(caracter("idk man, this works at 75 but i don't know why"))