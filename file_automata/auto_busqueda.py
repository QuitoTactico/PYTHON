import pyautogui as p
from random import randint
import time

# max  1365, 767
# cer  1344, 15
# min  1251, 13
# bus  500, 184
# vsc  395, 740

def random():
    for _ in range(10):
        x = randint(200, 1000)
        y = randint(200, 600)
        p.moveTo(x,y,0.2)
        time.sleep(0.1)

def centroAuto():
    p.moveTo(p.locateCenterOnScreen(p.screenshot()), duration=0.3)

def cerrar():
    p.moveTo(1344, 15, 0.2)
    time.sleep(0.5)
    p.click()

def minimizar():
    p.moveTo(1251, 13, 0.2)
    time.sleep(0.5)
    p.click()

def posicion():
    p.displayMousePosition()

def buscar(texto):
    minimizar()
    p.moveTo(500, 184, 0.15)
    p.click()
    p.write(texto, 0.2)
    p.press("enter")

def volver():
    p.moveTo(395, 740, 0.2)

def main():
    text = input()
    random()
    centroAuto()
    buscar(text)
    volver()
    p.click()
    cerrar()

main()
#posicion()

