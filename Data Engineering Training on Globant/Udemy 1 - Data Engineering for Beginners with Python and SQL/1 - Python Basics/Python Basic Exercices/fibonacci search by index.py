def fib(n, found):
    if n in found: return found[n]

    res = fib(n-2, found) + fib(n-1, found)
    found[n] = res
    return res


def find_fibonacci(n):
    found = {0:0, 1:1}

    return fib(n, found)

print(find_fibonacci(10))