def sumaGrupos(objetivo: int, numeros: list):
    return equilibrador(numeros, objetivo, "", "")


def equilibrador(numeros: list, objetivo: int, usados: str, noUsados: str):
    if objetivo == 0:
        list2 = list(map(int, str(noUsados).split()))
        list2.extend(numeros)
        list2.sort()

        list1 = list(map(int, str(usados).split()))
        list1.sort()

        resultado = [list1, list2]

        return resultado
    else:
        caso1 = equilibrador(
            numeros[1:], objetivo - numeros[0], usados + " " + str(numeros[0]), noUsados
        )

        caso2 = equilibrador(
            numeros[1:], objetivo, usados, noUsados + " " + str(numeros[0])
        )

        if caso2 == -1:
            return caso1
        elif caso1 == -1:
            return caso2
        elif (caso1 == -1) and (caso2 == -1):
            return -1
        else:
            return -1


def s(n: list):
    if len(n) == 1:
        return n[0]
    actual = n[0]
    return actual + s(n[1:])


def equilibra(personas):
    return sumaGrupos(int(s(personas) / 2), personas)
