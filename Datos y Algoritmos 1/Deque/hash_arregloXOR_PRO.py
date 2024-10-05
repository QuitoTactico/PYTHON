from collections import deque


def arreglo(arr1: list, arr2: list):
    commh = {}
    commd = deque()
    for i in arr1 + arr2:
        commh[i] = 0
    for i in arr1 + arr2:
        commh[i] = commh[i] + 1
    for i in commh:
        if commh[i] == 1:
            commd.append(i)
    res = list(commd)
    res.sort()
    return res


a = [3]
b = [1, 2, 3]
print(arreglo(a, b))
