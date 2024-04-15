lista_tuplas = [(0, 'papa'),(1, 'pera'),(2, 'yuca'),(3, 'pene')]

                    # si a zip de mandas n cosas de dimensión m, te devuelve m cosas de dimensión n
                    # (x1, y1, z1), (x2, y2, z2), ...
                    # >> (x1, x2, ...), (y1, y2, ...), (z1, z2, ...) 
                    # imagina una matriz. agarra el corte de agrupación y lo voltea. corta para el otro lado

                        # toca desempaquetar con *. O sea, que eso se convierta en cada una de esas tuplas. 
                        # sacarlas de su [].
tupla_listas = list(zip(*lista_tuplas))

print(tupla_listas)  # >> [(0, 1, 2, 3), ('papa', 'pera', 'yuca', 'pene')]
print(*tupla_listas) # >> (0, 1, 2, 3) ('papa', 'pera', 'yuca', 'pene')
                     # los saqué de su lista

# también puedes desempaquetarlo al guardarlo en n variables. n debe coincidir con el número de items
indices, frutas = zip(*lista_tuplas)
indices2, frutas2 = tupla_listas
print(indices, frutas)   # >> (0, 1, 2, 3) ('papa', 'pera', 'yuca', 'pene')
print(indices2, frutas2) # >> (0, 1, 2, 3) ('papa', 'pera', 'yuca', 'pene')


