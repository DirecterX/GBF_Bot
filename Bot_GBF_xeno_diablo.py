import pyautogui
import time
import Function
time.sleep(1)
attack= True
auto_atk = True
#declare Variable
play = True
SelectQuest = True

while play: 
    
    try:
        start_time = time.time()
       
        if pyautogui.locateOnScreen('Pic/selectsummon.png',region=(1497,92,325,93),confidence=0.75)!=None: #check summon
            #Function.Summon_Select()
            pyautogui.click(1669,500)
            time.sleep(2)
            pyautogui.click(1746,762)
#        elif pyautogui.locateOnScreen('Pic/oksummon.png',region=(1699,706,103,150))!=None:     
#            Function.Summon_OK()          
        elif pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75)!=None: #Attack
            if attack == True:
                time.sleep(4.2)
                Function.Heal_atk(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75))        
                attack = False
            if auto_atk == True:   
                if Function.Auto_Atk(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75))=="Success":
                    auto_atk = False
            #print('Click "Attack"')              
        #elif pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146),confidence=0.75)!=None: 
            #pyautogui.click(pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146)))
        #    pyautogui.moveTo(1622,415)  
        #    time.sleep(32)
        #    print('Click "full"')      
                           
        elif pyautogui.locateOnScreen('Pic/expgain.png',region=(1536,244,257,400),confidence=0.75)!=None: #EXP Gain
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1500,450,300,400),confidence=0.75))
            time.sleep(0.5)
            pyautogui.click(1647,627)
            time.sleep(0.5)
            pyautogui.click(1640,664)
            time.sleep(3.5)
            pyautogui.click(1640,134)
            time.sleep(1)
            pyautogui.click(1640,134)
            attack = True
            auto_atk = True
        elif pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,400,200),confidence=0.75)!=None: #Play Again
            Function.Finish_PLAYAGAIN(pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96)))
        elif pyautogui.locateOnScreen('Pic/halonm.png',region=(1464,203,300,200),confidence=0.75)!=None:#Halo Nightmare Appeared
            pyautogui.click(pyautogui.locateOnScreen('Pic/claimloot.png',region=(1631,717,300,200),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/needap.png',region=(1521,293,236,123),confidence=0.75)!=None:
            Function.REAP()
        elif pyautogui.locateOnScreen('Pic/friendrequest.png',region=(1488,308,317,196),confidence=0.75)!=None:
            Function.Finish_CANCEL()
        elif pyautogui.locateOnScreen('Pic/useitem.png',region=(1581,399,125,67),confidence=0.75)!=None:
            curclick = pyautogui.locateOnScreen('Pic/useitem.png',region=(1581,399,125,67),confidence=0.75)
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(curclick[0]-100,curclick[1],200,500),confidence=0.75))
        #Event Finish
        elif pyautogui.locateOnScreen('Pic/eventitem.png',region=(1505,258,200,250),confidence=0.75)!=None:
            pyautogui.click(1648,800)
        elif pyautogui.locateOnScreen('Pic/eventhome.png',region=(1529,508,261,112),confidence=0.75)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/eventhome.png',region=(1529,508,261,112),confidence=0.75))
       ##Event Seed of Redemption    
        elif pyautogui.locateOnScreen('Pic/rbattle.png',region=(1425,696,253,300),confidence=0.75)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('Pic/rbattle.png',region=(1425,696,253,300),confidence=0.75))  #Raid Quest
       #Raid Battle
        elif pyautogui.locateOnScreen('Pic/showdown.png',region=(1519,243,261,104),confidence=0.75)!=None:
            pyautogui.click(1646,679)    
        #Free Quest Event
        elif pyautogui.locateOnScreen('Pic/strife.png',region=(1553,303,178,118),confidence=0.75)!=None:
             pyautogui.click(pyautogui.locateOnScreen('Pic/playevent.png',region=(1759,576,99,70),confidence=0.75))
        #trophy archive
        elif pyautogui.locateOnScreen('Pic/trophy.png',region=(1534,404,250,110),confidence=0.75)!=None:
            curclick=pyautogui.locateOnScreen('Pic/trophy.png',region=(1534,404,250,110),confidence=0.75)
            pyautogui.click(curclick[0]+72,curclick[1]+241)
            time.sleep(0.5)
        #New Loot
        elif pyautogui.locateOnScreen('Pic/newloot.png',region=(1545,130,200,100),confidence=0.75)!=None:
            curclick=pyautogui.locateOnScreen('Pic/newloot.png',region=(1545,130,200,100),confidence=0.75)
            pyautogui.click(curclick[0]+41,curclick[1]+481) 
        #Fate Episode Unlock
        elif pyautogui.locateOnScreen('Pic/epunlock.png',region=(1540,262,200,100),confidence=0.75)!=None:  
            curclick=pyautogui.locateOnScreen('Pic/epunlock.png',region=(1540,262,200,100),confidence=0.75)
            pyautogui.click(curclick[0]+75,curclick[1]+309)
        #new skill
        elif pyautogui.locateOnScreen('Pic/newskill.png',region=(1540,262,200,100),confidence=0.75)!=None: 
            curclick=pyautogui.locateOnScreen('Pic/newskill.png',region=(1540,262,200,100),confidence=0.75)
            pyautogui.click(curclick[0]+23,curclick[1]+243)
        #itempicking 
        elif pyautogui.locateOnScreen('Pic/itempick.png',region=(1503,270,270,100),confidence=0.75)!=None:
            Function.Item_Pick()
        elif pyautogui.locateOnScreen('Pic/beginners.png',region=(1528,400,280,200),confidence=0.75)!=None:
            pyautogui.click(1643,686)
        #UandF Raid
        elif pyautogui.locateOnScreen('Pic/event/UandF/prestige.png',region=(1410,642,450,400),confidence=0.75)!=None:
            curclick = pyautogui.locateOnScreen('Pic/event/UandF/prestige.png',region=(1410,642,450,400),confidence=0.75)
            pyautogui.click(curclick)
            time.sleep(1.5)
            pyautogui.click(curclick[0]+285,curclick[1]+93)
            time.sleep(0.5)
            pyautogui.click(curclick[0]+84,curclick[1]-139)
        elif pyautogui.locateOnScreen('Pic/dailymission.png',region=(1484,336,350,400))!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(1459,519,380,400),confidence=0.75))
        #Xeno After Claim Loot
        elif pyautogui.locateOnScreen('Pic/spquest.png',region=(1563,468,150,200),confidence=0.75)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/spquest.png',region=(1563,468,150,200),confidence=0.75))
        #Xeno Select Quest
        elif pyautogui.locateOnScreen('Pic/event/Xeno/Diablo/DiabloLoop.png',region=(1414,350,470,608),confidence=0.85)!=None:         
            pos = pyautogui.locateOnScreen('Pic/event/Xeno/Diablo/DiabloLoop.png',region=(1414,350,470,608),confidence=0.85)
            pyautogui.click(pyautogui.locateOnScreen('Pic/playevent.png',region=(pos[0],pos[1],500,300),confidence=0.85))
            SelectQuest = True 
        elif pyautogui.locateOnScreen('Pic/event/Xeno/Diablo/DiabloClash.png',region=(1414,387,470,608),confidence=0.9)!=None:
            if SelectQuest == True:
                pos = pyautogui.locateOnScreen('Pic/event/Xeno/Diablo/DiabloClash.png',region=(1414,387,470,608),confidence=0.9)
                pyautogui.click(pyautogui.locateOnScreen('Pic/selectquest.png',region=(pos[0],pos[1],400,200),confidence=0.8))
                SelectQuest = False
              
       # else:    
        #    print("--- %s seconds ---" % (time.time() - start_time))

    except Exception as e:
        #play = False
        print(e)




