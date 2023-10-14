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
        elif pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218))!=None: #Attack
            if attack == True:
                time.sleep(2.8)
                #Function.Heal_atk(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218)))  
                Function.USE_SUMMON3(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218)))    
                attack = False
            #print('Click "Attack"')              
        elif pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146))!=None: 
            #pyautogui.click(pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146)))
            pyautogui.moveTo(1622,415)  
            time.sleep(32)
            print('Click "full"')      
                           
        elif pyautogui.locateOnScreen('Pic/expgain.png',region=(1536,339,257,200))!=None: #EXP Gain
            pyautogui.click(1640,528)
            time.sleep(0.5)
            pyautogui.click(1647,627)
            time.sleep(0.5)
            pyautogui.click(1640,664)
            time.sleep(2.5)
            pyautogui.click(1640,134)
            attack = True
        elif pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96))!=None: #Play Again
            Function.Finish_PLAYAGAIN(pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,242,96)))
        elif pyautogui.locateOnScreen('Pic/halonm.png',region=(1544,299,194,55))!=None:#Halo Nightmare Appeared
            Function.LMT_QUEST_LOOT(pyautogui.locateOnScreen('Pic/halonm.png',region=(1544,299,194,55)))
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
        elif pyautogui.locateOnScreen('Pic/event/charlotta/blumiel.png',region=(1557,396,317,200))!=None:
            curclick = pyautogui.locateOnScreen('Pic/event/charlotta/blumiel.png',region=(1557,396,317,200))
            pyautogui.click(curclick[0]+232,curclick[1]+84)
            time.sleep(1)
            pyautogui.click(curclick[0]+240,curclick[1]+157)
        elif pyautogui.locateOnScreen('Pic/spquest.png',region=(1437,513,422,120))!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/spquest.png',region=(1437,513,422,120)))
            time.sleep(0.5)
        #trophy achieved
        elif pyautogui.locateOnScreen('Pic/trophy.png',region=(1534,404,250,110))!=None:
            curclick=pyautogui.locateOnScreen('Pic/trophy.png',region=(1534,404,250,110))
            pyautogui.click(curclick[0]+72,curclick[1]+241)
            time.sleep(0.5)
        #New Loot
        elif pyautogui.locateOnScreen('Pic/newloot.png',region=(1545,130,200,100))!=None:
            curclick=pyautogui.locateOnScreen('Pic/newloot.png',region=(1545,130,200,100))
            pyautogui.click(curclick[0]+41,curclick[1]+481) 
        #Fate Episode Unlock
        elif pyautogui.locateOnScreen('Pic/epunlock.png',region=(1540,262,200,100))!=None:  
            curclick=pyautogui.locateOnScreen('Pic/epunlock.png',region=(1540,262,200,100))
            pyautogui.click(curclick[0]+75,curclick[1]+309)
        #new skill
        elif pyautogui.locateOnScreen('Pic/newskill.png',region=(1540,262,200,100))!=None: 
            curclick=pyautogui.locateOnScreen('Pic/newskill.png',region=(1540,262,200,100))
            pyautogui.click(curclick[0]+23,curclick[1]+243)
        #itempicking 
        elif pyautogui.locateOnScreen('Pic/itempick.png',region=(1503,270,270,100))!=None:
            Function.Item_Pick()
       # else:    
        #    print("--- %s seconds ---" % (time.time() - start_time))

    except Exception as e:
        play = False
        print(e)




