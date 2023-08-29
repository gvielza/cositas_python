from datetime import datetime
import webbrowser
import pyautogui as robot
import time
import pyperclip


url='https://www.bing.com/rewards/dashboard'
edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
response=webbrowser.get(edge_path).open(url)
fecha=datetime.now()
fecha_actual=f"{fecha.day}:{fecha.month}:{fecha.year}  {fecha.hour}:{fecha.minute}:{fecha.second}"


def obtener_puntaje():
    time.sleep(6)
    robot.moveTo(500,500)
    robot.doubleClick(500,500)
    robot.rightClick(500,500)
    time.sleep(5)
    robot.hotkey('ctrl', 'c')
    time.sleep(2)
    puntaje=pyperclip.paste()
    linea = fecha_actual + " El puntaje a la fecha es de: " + str(puntaje)
    with open('puntaje_bing.txt', "a+") as archivo:
        print(archivo.write(linea+'\n'))



obtener_puntaje()









#a+ crea el archivo para modo lectura y escritura y lo crea si no existe





print(fecha_actual)

