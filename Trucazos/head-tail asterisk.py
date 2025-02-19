head, *tail = [1,2,3,4,5]

print(head) # 1
print(tail) # [2, 3, 4, 5]

*head, tail = [1,2,3,4,5]

print(head) # [1, 2, 3, 4]
print(tail) # 5

# ahora adentro

# recuerda que head es una lista. al hacerle esto, metes todas sus weas como parámetro
print(*head, sep=' - ') # 1 - 2 - 3 - 4