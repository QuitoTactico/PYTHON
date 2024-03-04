import os, shutil
def arreglar(namecarp,namefile):
    shutil.copy(namecarp+'/'+namefile, namecarp+'/_'+namefile)
    new,i = open(namecarp+'/'+namefile,'w'),True
    with open(namecarp+'/_'+namefile, 'r') as fichero: 
        for linea in fichero:
            if linea[0] != '@': new.write(linea)
    new.write('}\n')
    new.close()
    os.remove(namecarp+'/_'+namefile)


for i in os.listdir():
    if '.' not in i:
        for j in os.listdir(i):
            if j.endswith('.css') == True: #guardar(i)
                arreglar(i,j)