from collections import deque


def arreglo(arr1: list, arr2: list):
    if arr1 == None or arr1 == [] or arr2 == None or arr2 == []:
        return None
    commh = {}
    commd = deque()
    """for i in arr1: comun[i] = 1
    for i in arr2:
        if i in comun: common.append(i)

    reslist = list(common)
    reslist.sort()"""

    for i in arr1 + arr2:
        commh[i] = 0
    for i in arr1 + arr2:
        commh[i] = commh[i] + 1

    for i in commh:
        if commh[i] == 1:
            commd.append(i)

    # print(commh)
    # print(commd)
    """arr1copy = arr1
    arr1copy.extend(arr2)
    print(arr1copy + arr2)
    print(arr1)"""
    res = list(commd)
    res.sort()
    return res

    # return reslist


a = [1, 2, 3, 4, 5, 6, -10, -20]
b = [9, 8, 7, 6, 5, 4, 999, 0, -10, 2, 888]
print(arreglo(a, b))
