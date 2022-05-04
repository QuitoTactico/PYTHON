from collections import deque
soldados = deque()

while True:
    try:   #esa mamada manda una excepción si está en un ciclo infinito wtf
        orden = input()
    
        if orden == None or orden == "" or orden == " ": break
        ordenlist = list(map(str,orden.split()))
    
        if ordenlist[0] == "MANDA":
            if len(soldados) == 0:
                print("IMPOSIBLE")
                continue
            print(soldados.popleft())
    
        if ordenlist[0] == "LLAMA":
            soldados.append(ordenlist[1])
            print(ordenlist[1])
    
        if ordenlist[0] == "AVR":
            print(list(soldados))
    except:
        break
