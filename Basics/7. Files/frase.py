def guardarFrase():
    f = open("frase.txt", "w")
    a = input()
    b = input()
    f.write(a + b)
