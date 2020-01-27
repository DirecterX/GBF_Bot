import pyautogui
import time
import Function
time.sleep(1)

#declare Variable
play = True

while play: 
    
    try:
        start_time = time.time()
       
        if pyautogui.locateOnScreen('Pic/selectsummon.png',region=(1497,92,325,93))!=None: #check summon
            Function.Summon_Select()
#        elif pyautogui.locateOnScreen('Pic/oksummon.png',region=(1699,706,103,150))!=None:     
#            Function.Summon_OK()          
        elif pyautogui.locateOnScreen('Pic/attack.png',region=(1673,403,246,200))!=None: #Attack
            Function.Battle_Attack(pyautogui.locateOnScreen('Pic/attack.png',region=(1673,403,246,200)))        
            #print('Click "Attack"')              
        elif pyautogui.locateOnScreen('Pic/semi.png',region=(1402,439,151,146))!=None: 
            Function.Battle_Auto()           
                           
        elif pyautogui.locateOnScreen('Pic/expgain.png',region=(1536,413,207,106))!=None: #EXP Gain
            Function.Finish_EXPGAIN()
        elif pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96))!=None: #Play Again
            Function.Finish_PLAYAGAIN(pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96)))
        elif pyautogui.locateOnScreen('Pic/halonm.png',region=(1528,310,235,85))!=None:#Halo Nightmare Appeared
            Function.HALO_NM()
        elif pyautogui.locateOnScreen('Pic/needap.png',region=(1521,293,236,123))!=None:
            Function.REAP()
        elif pyautogui.locateOnScreen('Pic/friendrequest.png',region=(1488,308,317,196))!=None:
            Function.Finish_CANCEL()
        elif pyautogui.locateOnScreen('Pic/useitemok.png',region=(1505,625,282,148))!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/useitemok.png',region=(1505,625,282,148)))

       # else:    
        #    print("--- %s seconds ---" % (time.time() - start_time))

    except Exception as e:
        play = False
        print(e)




