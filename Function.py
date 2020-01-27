import pyautogui
import time


def Summon_Select():

    pyautogui.click(pyautogui.locateOnScreen('Pic/rank.png',region=(1419,420,448,135)))
    time.sleep(2)
    pyautogui.click(1746,762)
    print('Select 1st summon')
        
        
def Summon_OK():
    
    if pyautogui.click(pyautogui.locateOnScreen('Pic/oksummon.png',region=(1627,643,262,207))):
        print('Click Button "OK"')      
        time.sleep(5) 
    else:
        print('Cannot Find Button "OK"')

def Battle_Attack(atklocate):
    pyautogui.click(atklocate)
    time.sleep(1)
    print('Click "Attack"')
 

def Battle_Auto():
    pyautogui.click(pyautogui.locateOnScreen('Pic/semi.png',region=(1402,439,151,146)))
    pyautogui.moveTo(1622,415)  
    time.sleep(32)
    print('Click "semi"')


def Finish_EXPGAIN():
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1497,551,310,176)))
    time.sleep(1)

def Finish_PLAYAGAIN(playagain):
    pyautogui.click(playagain)
    time.sleep(1)

def Finish_CANCEL():
    pyautogui.click(pyautogui.locateOnScreen('Pic/cancel.png',region=(1424,573,214,212)))
    time.sleep(1)

def REAP():
    #pyautogui.click(pyautogui.locateOnScreen('Pic/use.png',region=(1656,642,191,178)))
    pyautogui.click(1747,750)
    time.sleep(1)
    

def HALO_NM():
    pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(1429,713,217,165)))
    print("Close Click")
    time.sleep(1)
     
        
