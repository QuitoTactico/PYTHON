from dato import *

def generarDatos(n):
  lista = []
  if n>0:
    for i in range(n):
      lista.append(Dato())
  return lista
  