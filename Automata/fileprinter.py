import os

dir = os.path.abspath(os.getcwd())
dir_parent = dir[: dir.rfind("\\")]
back = "\\"
a = [0, 0]


def fileprinter(
    parent: str = dir, viewparent: bool = False, onlyfiles: bool = False, use=dir
):
    try:
        for i in os.listdir(parent):
            if i == "fileprinter.py":
                pass  # continue
            if "." in i:
                a[0] += 1
                if parent.replace(use, "") == "":
                    if viewparent:
                        print(parent.replace("\\", "/") + "/" + i)
                    else:
                        print(i)
                else:
                    if viewparent:
                        print(parent.replace("\\", "/") + "/" + i)
                    else:
                        print(parent.replace(use, "") + "/" + i)
            elif not onlyfiles:
                a[1] += 1
                if parent == None:
                    fileprinter(i, viewparent)
                else:
                    fileprinter(parent + "/" + i, viewparent, onlyfiles, use)
    except:
        if parent.replace(use, "") == "":
            if viewparent:
                print(parent.replace("\\", "/") + "/" + i)
            else:
                print(i)
        else:
            if viewparent:
                print(parent.replace("\\", "/") + "/" + i)
            else:
                print(parent.replace(use, "") + "/" + i)


def aux():
    opt = input("a. Actual dir  <-\np. Parent dir\nc. Custom dir\n>>")
    use = (
        dir_parent if opt == "p" else input("input the dir.\n->") if opt == "c" else dir
    )
    viewparent = (
        True
        if input("y. See parent (C:/...)\nn. Dont.                <-\n>>") == "y"
        else False
    )
    onlyfiles = (
        True
        if input("y. Just print files\nn. Search in carps (/.../...)   <-\n>>") == "y"
        else False
    )
    # IMPORTANTE PONER EL INPUT DE DIRECCIÓN EN ESTA VARIABLE Y NO ABAJO
    fileprinter(use, viewparent, onlyfiles, use)


aux()
print(f"{a[0]} archivos, {a[1]} carpetas")

# by Quito.
