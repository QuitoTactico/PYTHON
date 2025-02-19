from typing import List, Optional

# los valores default se evalúan cuando se procesa la función, no cuando se usa
# así que todos tendrían la misma lista como valor default, exactamente la misma lista, todos modificarán la misma si usan el valor default
# en vez de eso, mejor la inicializas como None, y que luego se le ponga el valor cada que se use


class Student:
    #def __init__(self, name: str, grades: list = []): # no
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        #self.grades = grades # no
        self.grades = grades or [] # si