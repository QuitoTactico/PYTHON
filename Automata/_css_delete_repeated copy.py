import os, shutil


def tojs(namecarp, namefile):
    new = open(namecarp + "/" + namefile[:-4] + ".js", "w")
    with open(namecarp + "/" + namefile, "r") as fichero:
        for linea in fichero:
            if linea[:-1] in d:
                i = False
            if i:
                new.write(linea)
            if linea == "}\n":
                i = True

    new.close()
    os.remove(namecarp + "/_" + namefile)


for i in os.listdir():
    if "." not in i:
        for j in os.listdir(i):
            if j.endswith(".jsx") == True:  # guardar(i)
                tojs(i, j)
