import time
import os 
import pyautogui
from time import sleep

# Abrindo Caculdadora
os.startfile(r'C:\Windows\System32\calc.exe')
time.sleep(5)

#Fazendo operação na caculadora 
#Click: Numero 2
pyautogui.click(349,564,duration=1)
#Click: Numero 0
pyautogui.click(350,631,duration=1)
#Click: Numero 2
pyautogui.click(349,564,duration=1)
#Click: Numero 2
pyautogui.click(349,564,duration=1)
#Click: Operação -
pyautogui.click(571,504,duration=1)
#Click: Numero 2
pyautogui.click(349,564,duration=1)
#Click: Numero 0
pyautogui.click(350,631,duration=1)
#Click: Numero 0
pyautogui.click(350,631,duration=1)
#Click: Numero 0
pyautogui.click(350,631,duration=1)
#Click: =
pyautogui.click(606,617,duration=1)





