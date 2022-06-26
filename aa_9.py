d,l = {},[]
with open('matrix.txt', 'r') as fichero: 
    for linea in fichero: 
        try:
            linea.index('Smith:')
            linea.index('?')
            for i in linea[7:].replace('? ?','?').replace('?','-?-').split('?'):
                if i not in d and i not in ['','\n','-'] and i[0] == '-' and i[-1] == '-' and i[1] != ' ' and i[-2] != ' ':
                    d[i] = True
                    l.append(i.replace('-','?'))
        except: pass
for i in l: print(i)