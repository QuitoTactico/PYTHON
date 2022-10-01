
from generarDato import *
from dato import *
from datos import *


def prueba1():
    print(generarNombreSexoEdad())

def prueba2(cantidad):
    muestra = generarDatos(cantidad)
    i=1
    for item in muestra:
      print(f'[{i}] : {item}')
      i+=1

#Prueba comparar
def prueba3():
    p1 = Dato()
    p2 = Dato()
    print(f'DATO P1: {p1.__dict__}')
    print(f'DATO P1: {p2.__dict__}')

    if p1 == p2:
      print("P1 y P2 Son iguales")
    else:
      print("P1 y P2 son diferentes")

    if p1 == p1:
      print("P1 y P1 Son iguales")
    else:
      print("P1 y P1 son diferentes")



if __name__ == "__main__":
  #print("-"*50)
  #print("Prueba 1: Generar Dato. ")
  #prueba1()
  #print("-"*50)

  print("Prueba 2: Generar Conjunto de datos. ")
  prueba2(int(input("Cantidad de datos a generar?: ")))
  print("-"*50)

  #print("Prueba 3: Comparar dos datos ")
  #prueba3()
  #print("-"*50)