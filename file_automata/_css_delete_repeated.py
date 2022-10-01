import os, shutil
d = {}
while(True):
    a = input()
    d[a] = True
    if a == '': break
print(d)
def delete(namecarp,namefile):
    shutil.copy(namecarp+'/'+namefile, namecarp+'/_'+namefile)
    new,i = open(namecarp+'/'+namefile,'w'),True
    with open(namecarp+'/_'+namefile, 'r') as fichero: 
        for linea in fichero:
            if linea[:-1] in d:
                i = False
            if i: new.write(linea)
            if linea == '}\n': i = True
    new.close()
    os.remove(namecarp+'/_'+namefile)


for i in os.listdir():
    if '.' not in i:
        for j in os.listdir(i):
            if j.endswith('.css') == True: #guardar(i)
                delete(i,j)