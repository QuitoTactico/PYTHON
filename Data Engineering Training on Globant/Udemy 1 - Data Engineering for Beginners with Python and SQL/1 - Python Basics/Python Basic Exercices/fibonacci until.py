def fibonacci(n):
    if n == 0: return []

    fib_series = [0, 1]
    
    while True:
        if fib_series[-1] >= n:
            return fib_series[:-1]
        else:
            fib_series.append(sum(fib_series[-2:]))


print(fibonacci(23))