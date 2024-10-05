from collections import deque


def arreglo(arr1, arr2):
    if arr1 == None or arr1 == [] or arr2 == None or arr2 == []:
        return None
    comun = {}
    res = deque()
    for i in arr1:
        comun[i] = 1
    for i in arr2:
        if i in comun:
            res.append(i)

    reslist = list(res)
    reslist.sort()
    return reslist


a = [1, 2, 3, 4, 5, 6]
b = [9, 8, 7]
print(arreglo(a, b))
