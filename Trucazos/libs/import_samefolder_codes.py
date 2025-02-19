import library_code
# para correr este código desde aquí
from library_code import library_function as lf1

# para correr este código desde afuera
# no se puede usar desde aquí. Sirve para que usen este mismo código desde afuera de la carpeta. Sirve porque como es una librería por el __init__, sabe dónde está ubicada. podrá buscar relativamente
from .library_code import library_function as lf2 

library_code.library_function() # ola, estoy en library_code. esta función está allí

lf1()
lf2() # se muere si no es de afuera