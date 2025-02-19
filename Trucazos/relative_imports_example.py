import libs.import_samefolder_codes

# así sí, porque tiene que estar afuera de la carpeta

# ya no sirve la línea normal (de ese código), pero la relatuva sí.
# los imports se refieren siempre desde el main en el que se ejecutan. este es main, y desde acá no se puede ver library code
# pero si se usara el relativo, ya sí se podría. lo que hace el relativo es simplemente ver que usé libs."algo", sabe que está en libs


# y puedo usar este! (comenta el de arriba)

import libs.sublib.import_outer_codes