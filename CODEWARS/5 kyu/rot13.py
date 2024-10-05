def rot13(message: str):
    letras = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    rot = ""
    for i in message:
        if i.isalpha():
            upperlower, i = i.isupper(), i.lower()
            nueva_letra = (
                letras[letras.index(i) + 13]
                if letras.index(i) + 13 < len(letras) - 1
                else letras[letras.index(i) + 13 - len(letras)]
            )
            rot += nueva_letra.upper() if upperlower else nueva_letra
        else:
            rot += i

    return rot
