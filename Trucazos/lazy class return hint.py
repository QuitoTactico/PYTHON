# como los métodos de las clases se procesan antes que las clases mismas
# un método podría retornar una clase que aún no "existe" mientras se procesa
# como cuando es la misma clase, u otra
# así que en vez de poner -> Class, ponemos -> "Class"

class Perro:                         #    HERE
    def __init__(self, nombre : str) -> "Perro":
        self.nombre = nombre

luna = Perro("Luna")