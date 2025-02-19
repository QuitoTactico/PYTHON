# no tienen nombre, pero si las metes en una variable pues sí las puedes llamar luego
add_lambda = lambda x, y: x + y

print(add_lambda(4, 2))

# puedes usarla inmediatamente, así:

(lambda x, y: x + y)(5, 7)   # retorna el resultado

print((lambda x, y: x + y)(5, 7))


# son muy útiles para pasar como parámetro, 
# por ejemplo ponerlas en un map() o en un apply() de pandas

nums = [1,2,3,4,5]

doubled1 = [(lambda x : x*2)(x) for x in nums]
doubled2 = map(lambda x : x*2, nums)

# como parámetros!
print(*doubled1)
# el map es un objeto perezoso, se muestra como "<map object at 0x00000202D9425120>"
print(*doubled2) 
# pero al desempaquetarlos, sí se recorre la lista para mostrarlos
# también con list()