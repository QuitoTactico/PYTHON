#Modifica el Fraccionario f1 sin problema, volvera a su valor original
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

class Fraccionario:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def mostrar(self):
        print(str(self.a)+"/"+str(self.b))
    
    def sumar(self, fraccionario2):
        c = lcm(self.b,fraccionario2.b)
        self.a = int((c/self.b*self.a)+(c/fraccionario2.b*fraccionario2.a))
        self.b = c
    
    def restar(self, fraccionario2):
        c = lcm(self.b,fraccionario2.b)
        self.a = int((c/self.b*self.a)-(c/fraccionario2.b*fraccionario2.a))
        self.b = c
    
    def multiplicar(self, fraccionario2):
        self.a *= fraccionario2.a
        self.b *= fraccionario2.b
    
    def dividir(self, fraccionario2):
        self.a *= fraccionario2.b
        self.b *= fraccionario2.a

# Toma de datos e impresion
x, y = map(int, input().split())
f1 = Fraccionario(x, y)

a, b = map(int, input().split())
f2 = Fraccionario(a, b)

# Original
f1.mostrar()

# Al sumar
f1.sumar(f2)
f1.mostrar()
f1 = Fraccionario(x, y)


# Al restar
f1.restar(f2)
f1.mostrar()
f1 = Fraccionario(x, y)


# Al multiplicar
f1.multiplicar(f2)
f1.mostrar()
f1 = Fraccionario(x, y)

# Al dividir
f1.dividir(f2)
f1.mostrar()