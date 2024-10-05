def search_index(lista, minmax):
    index = 0
    value = lista[0]

    for i, actual_value in enumerate(lista):
        if (
            minmax == "min"
            and actual_value < value
            or minmax == "max"
            and actual_value > value
        ):
            value = actual_value
            index = i

    return index


def queue_time(customers, n: int):
    queues = [0] * n

    for customer in customers:
        queues[search_index(queues, "min")] += customer

    return queues[search_index(queues, "max")]


print(queue_time([2, 3, 10], 2))


# YOU SILLY...


def queue_time(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
    return max(l)
