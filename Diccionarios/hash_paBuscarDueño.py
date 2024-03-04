def hasht(table : dict,val):
    valores = len(list(table.values()))
    for i in range(valores): 
        if int(valores[i]) == val: return list(table.keys())[i]