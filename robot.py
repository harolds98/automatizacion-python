import pyautogui as robot
import time

#para ver las cordenadas abrimos la terminal y abrimos python, aqui importamos pyautogui
#segido ejecutamos pyautogui.displayMousePosition() 
opera = 127, 549
direc = 1644, 46
boton1 = 1886, 410
boton01 = 1886, 352
boton2 = 1886, 585
exit = 2366, 10
reinicio = 1094, 53

time.sleep(3)
# Función para movilizar el mouse y dar un click


def abrir(pos, click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)


# Abrir google chrome
abrir(opera, click=2)

# Ubicarse en el buscador
time.sleep(3)
abrir(direc)
robot.typewrite("https://ouo.io/zYBlh3a")
robot.hotkey("enter")
time.sleep(5)

abrir(boton1)
time.sleep(2)
abrir(boton01)
time.sleep(5)
abrir(boton2)
time.sleep(2)
abrir(exit)
time.sleep(2)
abrir(reinicio)
print("finalizo el proceso")
