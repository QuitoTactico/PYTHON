#a = list(input())
#print(a[1])   

def plantavieja(b: list):
    a = [
        {"nombre":"Planta1","antiguedad":10},
        {"nombre":"Planta2","antiguedad":100},
        {"nombre":"Planta3","antiguedad":300}
        ]

    [{"nombre":"Planta1","antiguedad":10},{"nombre":"Planta2","antiguedad":100},{"nombre":"Planta3","antiguedad":300}]

    gan = 0

    if(b[0]["antiguedad"] < b[1]["antiguedad"]):
        gan = 1

    if(b[gan]["antiguedad"] < b[2]["antiguedad"]):
        gan = 2

    return(b[gan]["nombre"])