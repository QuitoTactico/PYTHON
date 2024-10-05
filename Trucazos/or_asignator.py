# Para simplificar las asignaciones por defecto cuando el valor ingresado puede dar None o False o 0, se puede usar el operador or, en vez del condicional ternario.
# Si el primer valor es false, seguirá y seguirá buscando en la expresión por cada or, hasta encontrar un valor que no sea False, None o 0. Ese lo devuelve.


diccionario = {"campaign_id": 30}

campaign_id_1 = diccionario["campaign_id"] if "campaign_id" in diccionario else 50
campaign_id_2 = diccionario.get("campaign_id") or 50
print(campaign_id_1, campaign_id_2)  # 30 30

# ------------------------------------------------------------

diccionario = {"NOT_campaign_id": 30}

campaign_id_1 = diccionario["campaign_id"] if "campaign_id" in diccionario else 50
campaign_id_2 = diccionario.get("campaign_id") or 50
print(campaign_id_1, campaign_id_2)  # 50 50

# ------------------------------------------------------------

# También funciona con listas vacías, diccionarios vacíos, etc. Ya que todo eso se toma como False.

diccionario = {}

campaign_id_1 = diccionario.get("campaign_id")  # None
campaign_id_2 = list(diccionario.keys())  # []
campaign_id_3 = len(diccionario.keys())  # 0
campaign_id_4 = 1 > 2  # False

campaign_id_5 = campaign_id_1 or campaign_id_2 or campaign_id_3 or campaign_id_4 or 50

print(campaign_id_5)  # 50

# ------------------------------------------------------------

"""
En Python, los siguientes valores se consideran False en un contexto booleano:

1. None
2. False
3. Cero de cualquier tipo numérico, por ejemplo, 0, 0.0, 0j.
4. Cualquier contenedor vacío, por ejemplo, '', (), [], {}, set(), range(0).
5. Instancias de clases definidas por el usuario, si la clase define un método __bool__() o __len__() que devuelve False o cero respectivamente.

Todos los demás valores se consideran True.
"""
