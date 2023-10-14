import pyautogui
import time
import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics
import multiprocessing

timeout = time.time() + 60*240

#Set which chara want to Use Skill 
Chara1Skill = False
Chara2Skill = False
Chara3Skill = False
Chara4Skill = False
SkillSw = True

UseSummon = True # wanna Use Summon
NoSummon = 1
SummonFirst = False # Use Summon First then Use Skill ?

PlayAgain = True # Play Again Button Click?

#Unite and Fight Setting
FarmMeat = True

Attack = True
Auto = True

atkIcon = True


def SetUpAttack():
    if SummonFirst == True and UseSummon==True:     # Use Summon Before Skill
        newFunction.Use_Summon(x,y,NoSummon) # No. Summon
        time.sleep(0.5)
        CharaUseSkill()
        SkillSw = False
    elif SummonFirst == False and UseSummon==True:  # Use Skill Before Summon
        CharaUseSkill()
        SkillSw = False
        time.sleep(0.5)
        newFunction.Use_Summon(x,y,NoSummon) # No. Summon
          
def CharaUseSkill(): # Set Skill 
    if SkillSw == True:
        if Chara1Skill == True:   # 1st Chara Skill // Parameter: Chara,Skill,Target
            newFunction.Use_Skill(x,y,1,1,0) # Chara,Skill,Target
            time.sleep(0.3)
            newFunction.Use_Skill(x,y,1,3,0)
            time.sleep(0.5)
            newFunction.Back_Button(x,y)      
        if Chara2Skill == True: # 2nd Chara Skill // Parameter: Chara,Skill,Target
            newFunction.Use_Skill(x,y,2,1,0) # Chara,Skill,Target
            time.sleep(0.5)
            newFunction.Back_Button(x,y) 
        if Chara3Skill == True: # 3rd Chara Skill // Parameter: Chara,Skill,Target
            newFunction.Use_Skill(x,y,3,3,0) # Using Skill 1
          #  time.sleep(0.3)
          #  newFunction.Use_Skill(x,y,3,2,0) # Using Skill 2
          #  time.sleep(0.3)
          #  newFunction.Use_Skill(x,y,3,3,0) # Using Skill 3
            time.sleep(0.5)
            newFunction.Back_Button(x,y) 
        if Chara4Skill == True: # 4th Chara Skill // Parameter: Chara,Skill,Target
            newFunction.Use_Skill(x,y,4,3,0) # Chara,Skill,Target
            time.sleep(0.5)
            newFunction.Back_Button(x,y) 
        
    



dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
red = win32api.RGB(255, 0, 0) # Red
Game_Detect = False
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
win = win32gui.FindWindow(None,'umamusume')
#win = win32gui.FindWindow(None,'Granblue Fantasy')
if not(win == 0):
    rect = win32gui.GetWindowRect(win)
    x = rect[0]
    y = rect[1]
    w = rect[2] 
    h = rect[3] 
    print("Window %s:" % win32gui.GetWindowText(win))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))
    Game_Detect = True
    past_coordinates = (x, y, w, h)
else:
    Game_Detect = False
    print('Not Found Game')
    
while Game_Detect: 
    try:
        test = 0
        start_time = time.time()
        #Close Exp Gain Popup When Quest Finish
        if pyautogui.locateOnScreen('Pic/expgain.png',region=(x+120,y+180,x+530,y+700),confidence=0.85)!=None:
            Attack = True
            SkillSw = True
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(x+120,y+450,x+530,y+650),confidence=0.9))
            print("Battle Finish")
            time.sleep(0.3)
       
        #Select Summon     
        elif pyautogui.locateOnScreen('Pic/selectsummon.png',region=(x+120,y+100,x+530,y+200),confidence=0.85)!=None:
            pyautogui.click(x+335,y+500)
            time.sleep(3)
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(x+120,y+450,x+530,y+900),confidence=0.9))
            time.sleep(0.3)
        #Attack Section
        elif pyautogui.locateOnScreen('Pic/attack.png',region=(x+340,y+455,x+550,y+550),confidence=0.85)!=None:
            if Attack == True:
                SetUpAttack()
                pyautogui.click(pyautogui.locateOnScreen('Pic/attack.png',region=(x+340,y+455,x+550,y+550),confidence=0.85))
                time.sleep(0.7)
                if Auto == True:
                    pyautogui.click(x+120,y+535)
                    #x+80,y+520,x+160,y+545 
                    if atkIcon == True :          
                        pyautogui.click(pyautogui.locateOnScreen('Pic/atkicon.png',region=(x+70,y+250,x+120,y+455),confidence=0.85))
                    time.sleep(0.3)
                    Attack = False
                print("Attack Phase")
        #got New Trophy
  #      elif pyautogui.locateOnScreen('Pic/atkicon.png',region=(x+70,y+250,x+120,y+455),confidence=0.85)!=None:
 #           if Auto == True:
 #               pyautogui.click(pyautogui.locateOnScreen('Pic/atkicon.png',region=(x+70,y+250,x+120,y+455),confidence=0.85))
        #got New Trophy
        elif pyautogui.locateOnScreen('Pic/trophy.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(x+120,y+500,x+530,y+800),confidence=0.9))
        #Fate Episode Unlocked
        elif pyautogui.locateOnScreen('Pic/epunlock.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(x+120,y+500,x+530,y+800),confidence=0.9))   
        #Unlock New Skills
        elif pyautogui.locateOnScreen('Pic/newskill.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(x+120,y+450,x+530,y+650),confidence=0.9))           
            time.sleep(0.3)  
        #Event Item 
        elif pyautogui.locateOnScreen('Pic/eventitem.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(x+120,y+450,x+530,y+900),confidence=0.9))           
            time.sleep(0.3) 
        #Extended Mastery Up
        elif pyautogui.locateOnScreen('Pic/exmastery.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            pyautogui.click(pyautogui.locateOnScreen('Pic/exmastery.png',region=(x+120,y+450,x+530,y+900),confidence=0.9))           
            time.sleep(0.3) 
        #Skyscope Quest Clear
        elif pyautogui.locateOnScreen('Pic/skyscope.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(x+120,y+450,x+530,y+900),confidence=0.9))           
            time.sleep(0.3)
        #Limited-Time Quest 
        elif pyautogui.locateOnScreen('Pic/limtime.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            if pyautogui.locateOnScreen('Pic/skip.png',region=(x+120,y+500,x+530,y+900),confidence=0.85)!=None: 
                pyautogui.click(pyautogui.locateOnScreen('Pic/skip.png',region=(x+120,y+500,x+530,y+900),confidence=0.9))     
                time.sleep(1)
            pyautogui.click(pyautogui.locateOnScreen('Pic/claimloot.png',region=(x+120,y+500,x+530,y+900),confidence=0.9))
        #Bonus Unlocked
        elif pyautogui.locateOnScreen('Pic/BonusUnlocked.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(x+120,y+450,x+530,y+900),confidence=0.9))           
            time.sleep(0.3) 
        #Clash Missions
        elif pyautogui.locateOnScreen('Pic/clashMission.png',region=(x+120,y+280,x+530,y+600),confidence=0.85)!=None:         
            pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(x+120,y+450,x+530,y+900),confidence=0.9))           
            time.sleep(0.3) 
        #Play Again Button Click
        elif pyautogui.locateOnScreen('Pic/playagain.png',region=(x+90,y+500,x+530,y+700),confidence=0.85)!=None:
            if PlayAgain == True:
                pyautogui.click(pyautogui.locateOnScreen('Pic/playagain.png',region=(x+90,y+500,x+530,y+700),confidence=0.85))           
                time.sleep(0.3)
        #Event Home
        elif pyautogui.locateOnScreen('Pic/eventhome.png',region=(x+90,y+550,x+530,y+700),confidence=0.85)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/eventhome.png',region=(x+90,y+550,x+530,y+700),confidence=0.85))           
            time.sleep(0.3)
    # Unite And fight (Guild War)--------------------------------------------
        #Unite And Fight Home Screen
        elif pyautogui.locateOnScreen('Pic/event/UandF/UandF.png',region=(x+120,y+100,x+530,y+200),confidence=0.85)!=None:
            if FarmMeat == True:               
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/Meat.png',region=(x+70,y+700,x+550,y+1000),confidence=0.9))
                time.sleep(1.5) 
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/MeatExtreme.png',region=(x+70,y+400,x+550,y+900),confidence=0.9)) 
            else:
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/Battle.png',region=(x+70,y+700,x+550,y+1000),confidence=0.9))
                time.sleep(1.5)  
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/ok.png',region=(x+70,y+400,x+550,y+900),confidence=0.9)) 
            time.sleep(0.3)           
        
        if time.time() > timeout:
            break
        
        
        time.sleep(0.1)
    except Exception as e:
        #play = False
        print(e)
    
