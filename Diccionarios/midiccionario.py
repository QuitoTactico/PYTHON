from ctypes import LibraryLoader


def chequeodiccionario(a):
    if(((a["nombre"]).startswith("C") == False) and (a["precio"] >= 300)):
        return True
    else:
        return False