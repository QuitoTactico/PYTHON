import os

proyect_name = 'futbol'
table_name = None 
# 0 = waiting | 1 = title info | 2 = reading info
mode = 0
fields = []
insert_str = ''
n = True 

output_file = open("csv_to_mysql_OUTPUT.txt", "w" , encoding="utf-8")

def conteo_data(data : list) -> int:
    n_data = 0
    for i in data:
        if i == "" or i == None: break
        n_data += 1
    return n_data

def print_table_name(table_name : str, fields : list) -> None:
    print(f'\n[ {table_name} ]',end='\n| ')
    for i in fields:
        print(i , end=' | ')
    print()

def sin_tildes(s : str) -> str:
    return s.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U')

def list_to_str(data : list , upper_comma : bool) -> str:
    return str(data)[1:-1] if upper_comma == False else str(data)[1:-1].replace("'","`")



def print_insert(insert_str , instance_data) -> None:
    output_file.write(insert_str + list_to_str(instance_data,False).replace("''", 'null') + ');\n')

def data_format(l : list) -> list:
    for i in range(len(l)):
        if l[i].count('/') == 2:
            l[i] = l[i].split('/')
            if len(l[i][-1]) == 4:
                l[i] = list(reversed(l[i]))
            l[i] = "-".join(l[i])
    return l

with open("csv_to_mysql_INPUT_2.csv", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        data = sin_tildes(linea[:-1]).split(';')
        num_data = conteo_data(data)
        
        if mode == 0:
            if num_data == 0: continue
            if num_data == 1: 
                table_name = data[0][1:].lower() if n else data[0].lower()
                mode = 1
                n= False
                continue

        if mode == 1:
            fields = [i.lower().replace('ñ','nn').replace(' ','_') for i in data[:num_data]]
            num_fields = len(fields)
            insert_str = f"INSERT INTO `{proyect_name}`.`{table_name}` ({list_to_str(fields,True)}) VALUES ("
            mode = 2
            print_table_name(table_name, fields)
            output_file.write('\n')
            continue

        if mode == 2:
            if num_data == 0:
                mode = 0
                continue

            instance_data = data_format(data[:num_fields])

            print_insert(insert_str, instance_data)

            print(end='|  ')
            for i in instance_data:
                print(i,end='\t')
            print()


output_file.close()


"INSERT INTO `futbol`.`jugadores` (`id_jugador`, `nombre`, `posicion`, `fecha_nto`) VALUES ('123', 'Juan Gomez', 'Delantero', '1987/02/10');"

f"INSERT INTO `{proyect_name}`.`{table_name}` ({list_to_str(fields,True)}) VALUES ("
