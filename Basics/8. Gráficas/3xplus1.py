import matplotlib.pyplot as plt


def collatz(n):
    n_inicial = n
    lista = [n]
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        lista.append(n)

    plt.plot(lista, "o-")
    plt.title(f"Collatz para n={n_inicial}")
    plt.xlabel(f"Iteración {len(lista)}")
    plt.ylabel(f"Valor de n {max(lista)}")
    plt.show()

    return {"n": n, "lista": lista}


if __name__ == "__main__":
    n = 0
    while True:
        n += 1
        o = input(f"Seguir? ({n}) -> ")
        if o in ["N", "n", "0"]:
            break
        else:
            try:
                n = int(o)
            except:
                pass
            collatz(n)
