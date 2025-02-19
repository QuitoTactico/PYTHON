# SE LLAMAN FUNCIONES DE PRIMERA CLASE
# son funciones usadas como variable en cualquier sentido

def funcion_principal():
    def funcion_anidada():
        print("¡Hola desde la función anidada!")

    return funcion_anidada


# Llamamos a la función principal para obtener la función anidada
mi_funcion = funcion_principal()

# Llamamos a la función anidada retornada
mi_funcion()
