arr = [0, 0, 3, 0, 0]


a, b = set(arr)  # devolverá a=0 y b=3, los diferentes. En un set nada se repite


print(arr.count(a))  # cuántas veces sale a?, dirá que 4

arr = [0, 0, 3, 0, 0, 4, 4, 6, 2, 2, 2]


diferentes = set(arr)

for i in diferentes:
    conteo = arr.count(i)
    print("el", i, "salió", conteo, "veces" if conteo != 1 else "vez")
