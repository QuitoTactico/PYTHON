# si me usan desde afuera, podré acceder a los códigos que hayan en mi carpeta padre
from ..library_code import library_function

library_function()

# de nuevo, sirve para que lo usen desde afuera
# si me llamaron como:
# import libs.sublib.import_outer_codes
# entonces yo podré usar cosas de libs.sublib