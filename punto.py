# Eliminar 'pass' y reemplazar por el codigo
import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanciaAlOrigen(self):
        return round((math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))),2)
    
    def anguloConElEjeX(self):
        return round((math.atan2(self.y,self.x)),2)
    
    def distanciaAOtroPunto(self, punto2):
        return round((math.sqrt(math.pow((self.x-punto2.x),2)+math.pow((self.y-punto2.y),2))),2)

# INPUT
x1, y1 =  map(int, input().split())
x2, y2 =  map(int, input().split())

punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)

print(punto1.distanciaAlOrigen())
print(punto1.anguloConElEjeX())
print(punto1.distanciaAOtroPunto(punto2))