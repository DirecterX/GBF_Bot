import pyautogui
import time
import keyboard

isClick = False
counter = 0

while True:
    if(isClick):
        if counter < 800:
            pyautogui.click(500,500)
           # counter+=1
        else:
            time.sleep(30)
            counter = 0
            #print("click")
    if keyboard.is_pressed('q'):
        isClick = True
    if keyboard.is_pressed('e'):
        isClick = False