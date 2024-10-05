def find_uniq(arr):
    num_primero = arr[0]
    num_segundo = arr[1]

    if num_primero != num_segundo:
        return arr[1] if arr[0] == arr[2] else arr[0]

    for i in arr:
        if i != num_primero:
            return i


print(find_uniq([0, 0, 0.55, 0, 0]))
