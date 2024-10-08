"""literal diccionarios
https://www.w3schools.com/python/python_ref_dictionary.asp

es un array innecesariamente homosexual
palabra -> definición/valor
llave -> valor
posición -> valor  (pero sería en lista)

aquí la posición literal tiene nombre en string

"""

# instanciación
tablahash = dict()  # lo volví diccionario, es eso mismo
tablahash = {}  # son sinónimos.
tablahash["polar"] = 123
tablahash["panda"] = 456
tablahash["pardo"] = 789
# llave     valor
#  {'polar': 123, 'panda': 456, 'pardo': 789}

print(tablahash)  #  {'polar': 123, 'panda': 456, 'pardo': 789}
print(tablahash.items())  # lista de parejas
print(tablahash.keys())  # lista de posiciones string
print(tablahash.values())  # lista de valores que tienen las pos

print(tablahash["polar"])  #  123  CAMBIAR VALOR
tablahash["polar"] = 777
print(tablahash["polar"])  #  777

print("polar" in tablahash)  # True     VER SI ESA POSICIÓN EXISTE
print("amogus" in tablahash)  # False

tablahash.pop("polar")  # ELIMINA ESA POSICIÓN Y LA RETORNA TMB
# no como las listas geis
print(tablahash)  # {'panda': 456, 'pardo': 789}
print(tablahash.pop("pardo"))  # 789  ELIMINÉ LA POS E IMPRIMÍ SU VALOR
print(tablahash)  # {'panda': 456}

print(hash("pardo"))  # int posición de memoria, pero es aleatorio e inútil
