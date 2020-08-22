import pyautogui
import time


def Summon_Select():

    pyautogui.click(pyautogui.locateOnScreen('Pic/rank.png',region=(1419,420,448,135),confidence=0.85))
    time.sleep(2)
    pyautogui.click(1746,762)
    print('Select 1st summon')
        
        
def Summon_OK():
    
    if pyautogui.click(pyautogui.locateOnScreen('Pic/oksummon.png',region=(1627,643,262,207),confidence=0.85)):
        print('Click Button "OK"')      
        time.sleep(5) 
    else:
        print('Cannot Find Button "OK"')

def Battle_Attack(atklocate):
    pyautogui.click(atklocate)
    time.sleep(1.5)
    pyautogui.click(1459,534)
    pyautogui.moveTo(1622,415)
    time.sleep(32)

    print('Click "Attack"')
 

def Battle_Auto():
    pyautogui.click(pyautogui.locateOnScreen('Pic/semi.png',region=(1402,439,151,146),confidence=0.85))
    pyautogui.moveTo(1622,415)  
    time.sleep(32)
    
    print('Click "semi"')


def Finish_EXPGAIN():
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1497,551,310,176),confidence=0.85))
    time.sleep(1)

def Finish_PLAYAGAIN(playagain):
    pyautogui.click(playagain)
    time.sleep(1)

def Finish_CANCEL():
    pyautogui.click(pyautogui.locateOnScreen('Pic/cancel.png',region=(1424,573,214,212),confidence=0.85))
    time.sleep(1)

def REAP():
    #pyautogui.click(pyautogui.locateOnScreen('Pic/use.png',region=(1656,642,191,178)))
    #curclick = pyautogui.locateOnScreen('Pic/use.png.png',region=(1521,293,236,123))
    pyautogui.click(pyautogui.locateOnScreen('Pic/use.png',region=(1634,438,200,500),confidence=0.85))
    time.sleep(1)
    
def LMT_QUEST_LOOT(pos):
    pyautogui.click(pos[0]+189,pos[1]+521)
    time.sleep(1)

def HALO_NM():
    pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(1429,713,217,165),confidence=0.85))
    print("Close Click")
    time.sleep(1)
     
def Heal_atk(atkpos):        
    pyautogui.click(atkpos[0]+348,atkpos[1]-227)
    time.sleep(1.5)
    #pyautogui.click(atkpos[0]+21,atkpos[1]-194)
    return 'battle start'

def USE_SUMMON1(summon_pos):
    pyautogui.click(summon_pos[0]+372,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(summon_pos[0]+28,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8))
    time.sleep(0.5)
    Heal_atk(summon_pos)    

def USE_SUMMON2(summon_pos):
    pyautogui.click(summon_pos[0]+372,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(summon_pos[0]+118,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8))
    time.sleep(0.5)
    Heal_atk(summon_pos)
    #print(atk)

def USE_SUMMON3(summon_pos):
    pyautogui.click(summon_pos[0]+372,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(summon_pos[0]+188,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8))
    time.sleep(0.5)
    Heal_atk(summon_pos)

def USE_SUMMON4(summon_pos):
    pyautogui.click(summon_pos[0]+372,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(summon_pos[0]+268,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8))
    time.sleep(0.5)
    Heal_atk(summon_pos)

def USE_SUMMON5(summon_pos):
    pyautogui.click(summon_pos[0]+372,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(summon_pos[0]+338,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8))
    time.sleep(0.5)
    Heal_atk(summon_pos)

def USE_SUMMON6(summon_pos):
    pyautogui.click(summon_pos[0]+372,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(summon_pos[0]+408,summon_pos[1]-60)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8))
    time.sleep(0.5)
    Heal_atk(summon_pos)

def Item_Pick():
    pyautogui.click(1634,548)
    time.sleep(0.8)
    pyautogui.click(1634,598)
    time.sleep(0.8)
    pyautogui.click(1634,634)

def Auto_Atk(atkpos):
    if pyautogui.locateOnScreen('Pic/full.png',region=(atkpos[0]-30,atkpos[1]-256,100,100),confidence=0.75)!=None:
        pyautogui.click(pyautogui.locateOnScreen('Pic/full.png',region=(atkpos[0]-30,atkpos[1]-256,100,100),confidence=0.75))
        pyautogui.moveTo(1622,415)
        return "Success"
    elif pyautogui.locateOnScreen('Pic/semi.png',region=(atkpos[0]-30,atkpos[1]-256,100,100),confidence=0.75)!=None:
        pyautogui.click(pyautogui.locateOnScreen('Pic/semi.png',region=(atkpos[0]-30,atkpos[1]-256,100,100),confidence=0.75))
        pyautogui.moveTo(1622,415)
        return "Success"

def Katalina(pos):
    print("useskill Katalina")
    curclick = pyautogui.locateOnScreen('Pic/water/2nd.png',region=(pos[0],pos[1]-200,400,100),confidence=0.8)
    pyautogui.click(curclick)
    time.sleep(0.8)
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/katalina.png',region=(pos[0],pos[1]-200,700,300),confidence=0.8))
    time.sleep(0.8)
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/MC.png',region=(pos[0],pos[1]-400,300,300),confidence=0.8))
    time.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/nextchar.png',region=(pos[0]+400,pos[1]-120,150,150),confidence=0.8))
    time.sleep(0.8)
    

def Europa(pos):
    print("useskill Europa")
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/europa.png',region=(pos[0],pos[1]-200,700,300),confidence=0.8))
    print("click Europa")
    time.sleep(0.8)
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/MC.png',region=(pos[0],pos[1]-400,300,300),confidence=0.8))
    print("Click MC")
    time.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/nextchar.png',region=(pos[0]+400,pos[1]-120,150,150),confidence=0.8))
    
    time.sleep(0.8)
    
def Grea(pos):
    print("useskill Grea")
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/grea.png',region=(pos[0],pos[1]-200,700,300),confidence=0.8))
    time.sleep(0.8)
    pyautogui.click(pyautogui.locateOnScreen('Pic/water/MC.png',region=(pos[0],pos[1]-400,300,300),confidence=0.8))
    time.sleep(2)
   
