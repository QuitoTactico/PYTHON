def fib(n):
    if n < 0:
        # Negafibonacci
        # return fib(-n) if n % 2 == 0 else -fib(-n) # this is correct according to wikipedia, but...
        return (
            -fib(-n) if n % 2 == 0 else fib(-n)
        )  # this was correct according to the kata, who knows
    return fib_iter(1, 0, 0, 1, n)


def fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    elif count % 2 == 0:
        p_prime = p * p + q * q
        q_prime = 2 * p * q + q * q
        return fib_iter(a, b, p_prime, q_prime, count // 2)
    else:
        return fib_iter(a * q + b * q + a * p, b * p + a * q, p, q, count - 1)
