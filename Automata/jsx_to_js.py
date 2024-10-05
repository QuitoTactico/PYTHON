import os, shutil


def tojs(namecarp: str, namefile: str):
    l = []
    n = []
    new = open(namecarp + "/" + namefile.replace(".jsx", ".js"), "w")
    with open(namecarp + "/" + namefile, "r") as fichero:
        for linea in fichero:
            if ".png" in linea:
                sep = linea.split()
                l.append(sep[1].replace("id=", "")[1:-1])
                n.append(sep[-3])
    new.write(
        f'import React from "react";\nimport "./{namefile.replace(".jsx",".css")}";\n'
    )
    for i in range(len(l)):
        new.write(f'import {l[i]} from "../../core/assets/{n[i]}";\n')
    i = 0
    new.write("\nconst " + namecarp + " = () => {\n\nreturn (\n")

    with open(namecarp + "/" + namefile, "r") as fichero:
        for linea in fichero:
            if ".png" in linea:
                new.write('<img id="' + l[i] + '" src={' + l[i] + "}/>\n")
                i += 1
            else:
                new.write(linea)

    new.write(");\n}\n\nexport default " + namecarp + ";\n")
    new.close()
    os.remove(namecarp + "/" + namefile)


for i in os.listdir():
    if "." not in i and i not in ["Home", "Contacto"]:
        for j in os.listdir(i):
            if j.endswith(".jsx") == True:  # guardar(i)
                tojs(i, j)
