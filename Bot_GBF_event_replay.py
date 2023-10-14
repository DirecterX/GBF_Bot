import pyautogui
import time
import Function
time.sleep(1)
attack= True
#declare Variable
play = True

while play: 
    
    try:
        start_time = time.time()
       
        if pyautogui.locateOnScreen('Pic/selectsummon.png',region=(1497,92,325,93))!=None: #check summon
            #Function.Summon_Select()
            pyautogui.click(1669,500)
            time.sleep(2)
            pyautogui.click(1746,762)
#        elif pyautogui.locateOnScreen('Pic/oksummon.png',region=(1699,706,103,150))!=None:     
#            Function.Summon_OK()          
        elif pyautogui.locateOnScreen('Pic/atkreplay.png',region=(1673,403,246,200))!=None: #Attack
            if attack == True:
                Function.Battle_Attack(pyautogui.locateOnScreen('Pic/atkreplay.png',region=(1673,403,246,200)))        
                attack = False
            #print('Click "Attack"')              
        elif pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146))!=None: 
            #pyautogui.click(pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146)))
            pyautogui.moveTo(1622,415)  
            time.sleep(32)
            print('Click "full"')      
                           
        elif pyautogui.locateOnScreen('Pic/expgain.png',region=(1536,413,207,106))!=None: #EXP Gain
            pyautogui.click(1647,627)
            attack = True
        elif pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96))!=None: #Play Again
            Function.Finish_PLAYAGAIN(pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96)))
        elif pyautogui.locateOnScreen('Pic/halonm.png',region=(1528,310,235,85))!=None:#Halo Nightmare Appeared
            Function.HALO_NM()
        elif pyautogui.locateOnScreen('Pic/needap.png',region=(1521,293,236,123))!=None:
            Function.REAP()
        elif pyautogui.locateOnScreen('Pic/friendrequest.png',region=(1488,308,317,196))!=None:
            Function.Finish_CANCEL()
        elif pyautogui.locateOnScreen('Pic/useitem.png',region=(1581,399,125,67))!=None:
            pyautogui.click(1643,705)
        #Event Finish
        elif pyautogui.locateOnScreen('Pic/eventitem.png',region=(1586,265,124,105))!=None:
            pyautogui.click(1648,800)
        elif pyautogui.locateOnScreen('Pic/eventhome.png',region=(1529,508,261,112))!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/eventhome.png',region=(1529,508,261,112)))
       ##Event Spaghetti Syndrome     
        elif pyautogui.locateOnScreen('Pic/raid.png',region=(1425,696,253,118))!=None:              
            pyautogui.click(pyautogui.locateOnScreen('Pic/raid.png',region=(1425,696,253,118)))  #Raid Quest
       #Raid Battle
        elif pyautogui.locateOnScreen('Pic/showdown.png',region=(1519,243,261,104))!=None:
            pyautogui.click(1646,679)    
        #Free Quest Event
        elif pyautogui.locateOnScreen('Pic/strife.png',region=(1553,303,178,118))!=None:
             pyautogui.click(pyautogui.locateOnScreen('Pic/playevent.png',region=(1759,576,99,70)))

       # else:    
        #    print("--- %s seconds ---" % (time.time() - start_time))

    except Exception as e:
        play = False
        print(e)




