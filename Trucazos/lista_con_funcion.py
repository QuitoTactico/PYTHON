# lista = [(valor | ternario) for valor in iterable (Nada | else valor condición_existencia)]

numeros = list(range(9))    # [0,1,2,3,4,5,6,7,8] 

lista = [i*10 for i in numeros]
print(lista)  # >> [10, 20, 30, 40, 50, 60]

# y ahora con condiciones de existencia, va después del for. AHORA PUEDE NO INCLUIR ESA POS
lista = [i*10 for i in numeros if i%2 == 0]
print(lista) # >> [0, 20, 40, 60, 80]


# condiciones de valor se ponen antes del for, con ternarios. TODAS LAS POSICIONES DEBEN DAR UN VALOR, NECESITA ELSE
lista = [i*10 if i%2 == 0 else 999 for i in numeros]
print(lista) # >> [0, 999, 20, 999, 40, 999, 60, 999, 80]

lista = [i*10 if i%2 == 0 else None for i in numeros] # el none no desaparece la posición
print(lista) # >> [0, None, 20, None, 40, None, 60, None, 80]


# metámosle un enumerate bien chistoso
lista_items = ['papa', 'pera', 'yuca', 'pene']
lista = [item.upper() for i,item in enumerate(lista_items) if i%2 == 0]
print(lista) # >> ['PAPA', 'YUCA']


