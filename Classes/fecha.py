# Eliminar 'pass' y reemplazar por el codigo
class Fecha:
    def __init__(self, d, m, a):
        self.d = d
        self.m = m
        self.a = a
    
    def string(self):
        return (str(str(self.d)+"-"+str(self.m)+"-"+str(self.a)))
        
    def comparar(self, fecha2):
        fe1 = self.d+(self.m*100)+(self.a*1000000)
        fe2 = fecha2.d+(fecha2.m*100)+(fecha2.a*1000000)
        if(fe1==fe2):
            return "iguales"
        elif(fe1<fe2):
            return "antes"
        elif(fe1>fe2):
            return "despues"

d, m, a = map(int, input().split())
f1 = Fecha(d, m, a)

d, m, a = map(int, input().split())
f2 = Fecha(d, m, a)

print(f1.string())
print(f1.comparar(f2))