import pyautogui as robot
import pyautogui, time

# para ver las cordenadas abrimos la terminal y abrimos python, aqui importamos pyautogui
# segido ejecutamos pyautogui.displayMousePosition()
opera = 127, 549
direc = 1644, 46
boton1 = 1596, 170
boton2 = 1480, 16
boton4 = 1765, 98
boton6 = 1888, 678
boton8 = 1900, 275
exit = 2366, 10
cerrar = 1930, 410
reinicio = 1162, 55
reinicio2 = 1018, 90


# Función para movilizar el mouse y dar un click
def abrir(pos, click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)


time.sleep(2)

# Abrir google chrome
abrir(opera, click=2)

# Ubicarse en el buscador
time.sleep(4)
abrir(direc)
robot.typewrite("https://cutw.in/vNX0zz")
time.sleep(2)
robot.hotkey("enter")

time.sleep(10)
abrir(boton1)
time.sleep(2)
abrir(boton2)
time.sleep(2)
abrir(boton1)
time.sleep(2)
pyautogui.scroll(-410)
time.sleep(2)

abrir(boton4)
time.sleep(24)
abrir(boton6)
time.sleep(3)
abrir(boton2)
time.sleep(3)
abrir(boton1)
time.sleep(2)
pyautogui.scroll(-320)
time.sleep(32)
abrir(boton8)
time.sleep(2)
abrir(boton2)
time.sleep(4)
abrir(exit)
time.sleep(2)
abrir(cerrar)
time.sleep(2)
abrir(reinicio)
time.sleep(2)
abrir(reinicio2)



