with open("trifelios.txt", "r") as fichero:
    for linea in fichero:
        res, l = "No es trifelio", list(map(str, linea.replace("\n", "").split("-")))
        for i in range(len(l[0])):
            if l[0][i:] + l[0][:i] == l[1]:
                res = "Es trifelio"
        print(res)
