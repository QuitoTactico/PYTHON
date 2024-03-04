from generarDato import *

class Dato:
  def __init__(self):
    dato = generarNombreSexoEdad()
    self.nombre = dato['nombre']
    self.sexo = dato['sexo']
    self.edad = dato['edad']
    self.nacionalidad = dato['nacionalidad']
  
  #==
  def __eq__ (self, __o: object) -> bool:
    return (self.edad == __o.edad) #and (self.sexo == __o.sexo)

  #<
  def __lt__ (self, __o: object) -> bool:
    return (self.edad< __o.edad) #and (self.sexo == __o.sexo)
  
  #<=
  def __le__ (self, __o: object) -> bool:
    return (self.edad <= __o.edad) #and (self.sexo == __o.sexo)
  
  #>
  def __gt__ (self, __o: object) -> bool:
    return (self.edad > __o.edad) #and (self.sexo == __o.sexo)
  
  #>=
  def __ge__ (self, __o: object) -> bool:
    return (self.edad >= __o.edad) #and (self.sexo == __o.sexo)
  
  #!=
  def __ne__ (self, __o: object) -> bool:
    return (self.edad != __o.edad) #or (self.sexo != __o.sexo)

  def __str__(self):
    return f'Objeto Dato=[nombre: {self.nombre}, edad: {self.edad}, sexo: {self.sexo}, nacionalidad: {self.nacionalidad}]'
  
  