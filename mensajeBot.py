import pyautogui as robot
import pyautogui
import time

#las posisciones a donde se dirige el mouse
minimiza = 1251, 18
what = 22, 241

#definimos abrir para que cuando se llame a alguna posicion se de click
def abrir(pos, click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

#time.sleep sera el tiempo que se demora en ejecutar la sigiente accion
time.sleep(2)
#da un click en la posicion minimiza
abrir(minimiza)
time.sleep(2)
abrir(what)
time.sleep(2)

# 20 es la cantidad de veces que se va a repetir el mensaje
for i in range(20):
    # escribe el mensaje que esta entre comillas
    pyautogui.typewrite("Eres una perra...")
    # da enter y envia el mensaje
    pyautogui.press("enter")
