from colorama import Fore, Back, Style
#Datos
#Nodo -> Paises
#Vertices -> Fronteras
paises = ['Colombia', 'Venezuela', 'Brasil', 'Peru', 'Bolivia', 'Ecuador', 'Guyana', 'Guayana Francesa', 'Surinam', 'Uruguay', 'Paraguay', 'Argentina', 'Chile']
fronteras = {}
# key: paise, y value:paises con los que tiene frontera
fronteras['Colombia']=['Venezuela', 'Brasil', 'Peru', 'Ecuador']
fronteras['Venezuela']=['Colombia','Brasil','Guyana']
fronteras['Peru']=['Colombia', 'Ecuador', 'Chile', 'Bolivia', 'Brasil']
fronteras['Brasil']=['Colombia', 'Venezuela', 'Peru', 'Bolivia', 'Guayana Francesa', 'Surinam', 'Uruguay', 'Paraguay', 'Argentina']
fronteras['Bolivia']=['Brasil', 'Peru', 'Paraguay', 'Argentina', 'Chile']
fronteras['Ecuador']=['Colombia', 'Peru']
fronteras['Guyana']=['Venezuela', 'Brasil', 'Surinam']
fronteras['Guayana Francesa']=['Brasil', 'Surinam']
fronteras['Surinam']=['Brasil', 'Guyana', 'Guayana Francesa']
fronteras['Uruguay']=['Brasil','Argentina']
fronteras['Paraguay']=['Brasil','Bolivia','Argentina']
fronteras['Argentina']=['Brasil', 'Bolivia', 'Uruguay', 'Paraguay', 'Chile']
fronteras['Chile']=['Peru', 'Bolivia','Argentina']
colores = [Fore.GREEN, Fore.BLUE, Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
#=================================
colorPaises = {}
def validarColor(nodo, color):
    for frontera in fronteras[nodo]:
        colorFrontera = colorPaises.get(frontera)
        if colorFrontera == color:
            return False
    return True
def pintarPais(nodo):
    for color in colores:
        if validarColor(nodo, color):
            return color
def programa():
    for pais in paises:
        colorPaises[pais] = pintarPais(pais)
    
    #ver resultados
    for pais in paises:
        print(colorPaises[pais]+ Back.BLACK + f' {pais} ' +  Style.RESET_ALL)
if __name__ == '__main__':
    programa()
