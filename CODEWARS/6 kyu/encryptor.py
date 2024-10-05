def decrypt(encrypted_text, n):
    if encrypted_text is None or len(encrypted_text) == 0 or n < 1:
        return encrypted_text

    lista = [0] * len(encrypted_text)

    for _ in range(n):
        pos = 1

        for i in encrypted_text:
            if pos > len(encrypted_text) - 1:
                pos = 0

            lista[pos] = i
            pos += 2
        encrypted_text = "".join(lista)

    return encrypted_text


def decrypt_jonathan(encrypted_text, n):
    if encrypted_text == "" or n == 0:
        return encrypted_text

    while n > 0:
        i = 0
        texto = encrypted_text
        encrypted_text = list(encrypted_text)
        total = []
        listaimpares = []

        largo = len(texto)

        for i in range(len(encrypted_text) // 2):
            listaimpares.append(texto[i])
            encrypted_text.pop(0)
        # print(len(encrypted_text))

        i = 0
        while i < len(encrypted_text) - 1:
            total += encrypted_text[i]
            total += listaimpares[i]
            # print(total)
            # print(i)
            i += 1
        # print(listaimpares)
        # print(encrypted_text)
        # encrypted_text = texto
        # encrypted_text = list(encrypted_text)
        n -= 1
        # print(i)
        # print(encrypted_text[i])
        if largo % 2 != 0:
            total += texto[-1]
        else:
            total += texto[-1] + listaimpares[-1]
        encrypted_text = "".join(total)

    # print(i)
    # print(total)
    return "".join(total)


def encrypt(text, n):
    if text is None or len(text) == 0 or n < 1:
        return text

    lista = [0] * len(text)

    for _ in range(n):
        pos = 1

        for i in range(len(lista)):
            if pos > len(text) - 1:
                pos = 0

            lista[i] = text[pos]
            pos += 2
        text = "".join(lista)

    return text
