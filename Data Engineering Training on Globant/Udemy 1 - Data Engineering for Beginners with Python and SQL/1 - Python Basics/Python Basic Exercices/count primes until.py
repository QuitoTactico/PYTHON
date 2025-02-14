def count_primes(n):
    primes = set(range(2, n))

    for i in range(2, n):
        times = int(n / i) + 1

        for mult in range(2, times):
            primes.discard(i*mult)

    print(primes)
    return len(primes)


print(count_primes(10))