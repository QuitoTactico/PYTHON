def sort_array(lista):
    odd = []
    for i in lista:
        if i % 2 == 1:
            odd.append(i)

    odd.sort(reverse=True)

    return [i if i % 2 == 0 else odd.pop() for i in lista]

print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))