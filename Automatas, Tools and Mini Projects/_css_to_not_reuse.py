import os


def guardar(name):
    new, i = open("_res_css.txt", "w"), True
    with open(name, "r") as fichero:
        for linea in fichero:
            if i == True and linea != "\n":
                new.write(linea)
                i = False
            if linea == "}\n":
                i = True
    new.close()


for i in os.listdir():
    if i.endswith(".css") == True:
        guardar(i)
