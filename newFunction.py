    
import pyautogui
import time

    
def Use_Summon(x,y,summon):
    
    pyautogui.click(x+460,y+650) # Select Summon
    time.sleep(0.7)
        
    if summon == 1:         
        pyautogui.click(x+120,y+645)
    elif summon == 2:
        pyautogui.click(x+195,y+645)
    elif summon == 3:
        pyautogui.click(x+270,y+645)
    elif summon == 4:
        pyautogui.click(x+350,y+645)
    elif summon == 5:
        pyautogui.click(x+425,y+645)
    elif summon == 6:
        pyautogui.click(x+505,y+645)
        
    time.sleep(1)
    pyautogui.click(pyautogui.locateOnScreen('Pic/oksummon.png',region=(x+320,y+550,x+530,y+700),confidence=0.85))
    
    print("Using Summon"+str(summon))
    time.sleep(0.5)
    #SUMMON
    #DrawRect(x+420,y+570,x+500,y+720) # Select Summon
    #DrawRect(x+85,y+570,x+155,y+720) # Summon1     x+120,y+645
    #DrawRect(x+160,y+570,x+230,y+720) # Summon2    x+195,y+645
    #DrawRect(x+235,y+570,x+310,y+720) # Summon3    x+270,y+645
    #DrawRect(x+315,y+570,x+385,y+720) # Summon4    x+350,y+645
    #DrawRect(x+390,y+570,x+460,y+720) # Summon5    x+425,y+645
    #DrawRect(x+470,y+570,x+540,y+720) # Summon6    x+505,y+645
    
def Select_Chara(x,y,chara):
    if chara == 1:
        pyautogui.click(x+120,y+645)
    elif chara == 2:
        pyautogui.click(x+200,y+645)
    elif chara == 3:
        pyautogui.click(x+280,y+645)
    elif chara == 4:
        pyautogui.click(x+365,y+645)

    print("Select Character "+str(chara))
    #CHARACTER 
    #DrawRect(x+85,y+570,x+400,y+720) # Character
    #DrawRect(x+85,y+570,x+155,y+720) # Chara 1  x+120,y+645
    #DrawRect(x+165,y+570,x+235,y+720) # Chara 2 x+200,y+645
    #DrawRect(x+245,y+570,x+320,y+720) # Chara 3 x+280,y+645
    #DrawRect(x+330,y+570,x+400,y+720) # Chara 4 x+365,y+645
    
def Skill(x,y,skill):
    if skill == 1:
        pyautogui.click(x+225,y+675)
    elif skill == 2:
        pyautogui.click(x+310,y+675)
    elif skill == 3:
        pyautogui.click(x+395,y+675)
    elif skill == 4:
        pyautogui.click(x+480,y+675)
    
    #SKILL 
    #DrawRect(x+200,y+650,x+505,y+700) # SKILL
    #DrawRect(x+200,y+650,x+250,y+700) # SKILL 1 x+225,y+675
    #DrawRect(x+285,y+650,x+335,y+700) # SKILL 2 x+310,y+675   
    #DrawRect(x+370,y+650,x+420,y+700) # SKILL 3 x+395,y+675
    #DrawRect(x+455,y+650,x+505,y+700) # SKILL 4 x+480,y+675
    
def Use_Skill_On(x,y,target):
    
    if target == 1:
        pyautogui.click(x+220,y+407)
    elif target == 2:
        pyautogui.click(x+310,y+407)
    elif target == 3:
        pyautogui.click(x+405,y+407)
    elif target == 4:
        pyautogui.click(x+220,y+577)
    elif target == 5:
        pyautogui.click(x+310,y+577)
    elif target == 6:
        pyautogui.click(x+405,y+577)   
    #SKILL ON Character
    #DrawRect(x+180,y+330,x+440,y+650) # ALL CHARA
    #DrawRect(x+185,y+335,x+255,y+480) # ON MC          x+220,y+407
    #DrawRect(x+275,y+335,x+350,y+480) # ON 2nd Chara   x+310,y+407
    #DrawRect(x+370,y+335,x+440,y+480) # ON 3rd Chara   x+405,y+407
    #DrawRect(x+185,y+505,x+255,y+650) # ON 4th Chara   x+220,y+577
    #DrawRect(x+275,y+505,x+350,y+650) # ON 5th Chara   x+310,y+577
    #DrawRect(x+370,y+505,x+440,y+650) # ON 6th Chara   x+405,y+577
    
def Use_Skill(x,y,chara,skill,target): 
    
    Select_Chara(x,y,chara)
    time.sleep(0.5) 
    Skill(x,y,skill)
    time.sleep(0.5) 
    Use_Skill_On(x,y,target)
    time.sleep(0.5) 
    if(target==0):
        print("Character "+str(chara)+" Use Skill "+str(skill))
    else:
        print("Character "+str(chara)+" Use Skill "+str(skill)+" On Chara -> "+str(target))    
    
def Back_Button(x,y):
    pyautogui.click(pyautogui.locateOnScreen('Pic/back.png',region=(x+70,y+445,x+200,y+550),confidence=0.85))
    time.sleep(0.3)  