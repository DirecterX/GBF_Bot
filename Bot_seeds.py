import pyautogui
import time
import Function
time.sleep(1)
attack= True
auto_atk = True
useskill = False
katalina = False
europa = False
grea = False
character = "katalina"
#declare Variable
play = True
SelectQuest = True
FarmMeat = False

while play: 
    
    try:
        start_time = time.time()
       
        if pyautogui.locateOnScreen('Pic/selectsummon.png',region=(1497,92,325,93),confidence=0.75)!=None: #check summon
            #Function.Summon_Select()
            print("Select Summon")
            pyautogui.click(1669,500)
            time.sleep(2)
            pyautogui.click(1746,762)
            attack = True
            auto_atk = True
#        elif pyautogui.locateOnScreen('Pic/oksummon.png',region=(1699,706,103,150))!=None:     
#            Function.Summon_OK()
        elif pyautogui.locateOnScreen('Pic/expgain.png',region=(1536,200,300,400),confidence=0.75)!=None: #EXP Gain
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1500,450,300,600),confidence=0.75))
            print("Exp gain")
            attack = True
            auto_atk = True
        elif pyautogui.locateOnScreen('Pic/expGainG.png',region=(1536,200,300,400),confidence=0.75)!=None: #EXP Gain event
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1500,450,300,600),confidence=0.75))
            print("Exp gain")
            attack = True
            auto_atk = True
        elif pyautogui.locateOnScreen('Pic/BonusUnlocked.png',region=(1536,200,300,400),confidence=0.75)!=None: #EXP Gain event
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1500,450,300,600),confidence=0.75))
            print("Master Lvl Up")        
        elif pyautogui.locateOnScreen('Pic/atkicon.png',region=(1335,239,250,300),confidence=0.8)!=None:           
            pyautogui.click(pyautogui.locateOnScreen('Pic/atkicon.png',region=(1335,239,250,300),confidence=0.75))
            #katalina = True        
        elif pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75)!=None: #Attack
            pos = pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75)
            if attack == True:
                time.sleep(6)
                #Function.Heal_atk(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75))        
                Function.USE_SUMMON1(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75))
                attack = False
            if auto_atk == True:   
                if Function.Auto_Atk(pyautogui.locateOnScreen('Pic/heal.png',region=(1380,647,274,218),confidence=0.75))=="Success":
                    auto_atk = False
            #use Skill 
            if katalina == True:           
                Function.Katalina(pos)
                europa = True
                katalina = False
                grea = False
            if europa == True:
                Function.Europa(pos)
                europa = False
                katalina = False
                grea = True
            if grea == True:
                Function.Grea(pos)
                europa = False
                katalina = False
                grea = False

            #print('Click "Attack"')              
       # elif pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146))!=None: 
            #pyautogui.click(pyautogui.locateOnScreen('Pic/full.png',region=(1402,439,151,146)))
           # pyautogui.moveTo(1622,415)  
           # time.sleep(32)
            #print('Click "full"')      
                           
        
        elif pyautogui.locateOnScreen('Pic/halonm.png',region=(1464,203,300,200),confidence=0.75)!=None:#Halo Nightmare Appeared
            print("Claim Loot Special")
            pyautogui.click(pyautogui.locateOnScreen('Pic/claimloot.png',region=(1631,717,300,200),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/needap.png',region=(1521,293,236,123),confidence=0.75)!=None:
            print("Need AP")
            Function.REAP()
        elif pyautogui.locateOnScreen('Pic/friendrequest.png',region=(1488,308,317,196),confidence=0.75)!=None:
            print("Cancel Friend Request")
            Function.Finish_CANCEL()
        elif pyautogui.locateOnScreen('Pic/useitem.png',region=(1494,271,500,500),confidence=0.75)!=None:
            print("Re AP")
            curclick = pyautogui.locateOnScreen('Pic/useitem.png',region=(1494,271,300,300),confidence=0.75)           
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(curclick[0]-100,curclick[1],200,500),confidence=0.75))
        #Event Finish
        elif pyautogui.locateOnScreen('Pic/eventitem.png',region=(1505,258,300,350),confidence=0.75)!=None:
            print("Collect Event Item")
            curclick = pyautogui.locateOnScreen('Pic/eventitem.png',region=(1505,258,300,350),confidence=0.75)
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(curclick[0]-100,curclick[1],200,500),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/eventhome.png',region=(1529,508,261,200),confidence=0.75)!=None:
            print("Event Home")
            pyautogui.click(pyautogui.locateOnScreen('Pic/eventhome.png',region=(1529,508,261,112),confidence=0.75))
       ##Event Seed of Redemption    
        elif pyautogui.locateOnScreen('Pic/rbattle.png',region=(1425,696,253,300))!=None:    
            print("Raid Battle")          
            pyautogui.click(pyautogui.locateOnScreen('Pic/rbattle.png',region=(1425,696,253,300)))  #Raid Quest
       #Raid Battle
        elif pyautogui.locateOnScreen('Pic/showdown.png',region=(1519,243,261,104),confidence=0.75)!=None:
            print("ShowDown")
            pyautogui.click(1646,679)    
        #Free Quest Event
        elif pyautogui.locateOnScreen('Pic/strife.png',region=(1553,303,178,118),confidence=0.75)!=None:
             pyautogui.click(pyautogui.locateOnScreen('Pic/playevent.png',region=(1759,576,99,70),confidence=0.75))
        #trophy archive
        elif pyautogui.locateOnScreen('Pic/trophy.png',region=(1534,404,250,110),confidence=0.75)!=None:
            print("Got New Trophy")
            curclick=pyautogui.locateOnScreen('Pic/trophy.png',region=(1534,404,250,110),confidence=0.75)
            pyautogui.click(curclick[0]+72,curclick[1]+241)
            time.sleep(0.5)
        #New Loot
        elif pyautogui.locateOnScreen('Pic/newloot.png',region=(1545,130,200,100),confidence=0.75)!=None:
            print("Get new Loot")
            curclick=pyautogui.locateOnScreen('Pic/newloot.png',region=(1545,130,200,100),confidence=0.75)
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(curclick[0]-100,curclick[1],300,900),confidence=0.75)) 
        #Fate Episode Unlock
        elif pyautogui.locateOnScreen('Pic/epunlock.png',region=(1540,262,200,100))!=None:  
            print("Fate Episode Unlock")
            curclick=pyautogui.locateOnScreen('Pic/epunlock.png',region=(1540,262,200,100))
            pyautogui.click(curclick[0]+75,curclick[1]+309)
        #new skill
        elif pyautogui.locateOnScreen('Pic/newskill.png',region=(1540,262,200,300))!=None: 
            print("got new skill")
            curclick=pyautogui.locateOnScreen('Pic/newskill.png',region=(1540,262,200,300),confidence=0.75)
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(curclick[0]-100,curclick[1],300,500),confidence=0.75))
        #itempicking 
        elif pyautogui.locateOnScreen('Pic/itempick.png',region=(1503,254,300,300))!=None:
            print("Item Pick")
            Function.Item_Pick()
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1515,423,300,400),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/beginners.png',region=(1528,400,280,200))!=None:
            pyautogui.click(1643,686)
        elif pyautogui.locateOnScreen('Pic/event.png',region=(1498,483,450,500),confidence=0.99)!=None:
            print("event button click")
            pyautogui.click(pyautogui.locateOnScreen('Pic/event.png',region=(1498,483,450,500),confidence=0.99))
        #UandF Raid
        elif pyautogui.locateOnScreen('Pic/event/UandF/UandF.png',region=(1427,71,350,400),confidence=0.8)!=None:
            if FarmMeat == True:
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/Meat.png',region=(1340,540,560,499),confidence=0.8))
                time.sleep(1.5)
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/MeatExtreme.png',region=(1340,540,560,499),confidence=0.8))
                
            else:
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/battle.png',region=(1340,540,560,499),confidence=0.8))
                time.sleep(1.5)
                pyautogui.click(pyautogui.locateOnScreen('Pic/event/UandF/MeatExtreme.png',region=(1340,540,560,499),confidence=0.8))
        elif pyautogui.locateOnScreen('Pic/dailymission.png',region=(1484,336,350,400))!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(1459,519,380,400),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/rankrose.png',region=(1446,76,450,500),confidence=0.8)!=None:
            print("Rank up")
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1500,450,300,400),confidence=0.75))
            print("Extended Mastery up")
        elif pyautogui.locateOnScreen('Pic/exmastery.png',region=(1446,450,450,500),confidence=0.7)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/exmastery.png',region=(1500,450,300,400),confidence=0.75))   
        elif pyautogui.locateOnScreen('Pic/mcex.png',region=(1446,169,450,500),confidence=0.8)!=None:
            print("MC Extended Mastery Up")
            pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(1500,450,300,400),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/water/beware.png',region=(1485,232,300,300),confidence=0.8)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/water/extreme.png',region=(1413,513,450,350),confidence=0.8))
            #Select extreme or vh Here
        elif pyautogui.locateOnScreen('Pic/raid.png',region=(1410,660,450,400),confidence=0.85)!=None:
            print("go raid")
            curclick = pyautogui.locateOnScreen('Pic/raid.png',region=(1410,660,450,400),confidence=0.85)
            pyautogui.click(curclick)
            #time.sleep(1.5)
            #pyautogui.click(pyautogui.locateOnScreen('Pic/ok.png',region=(curclick[0],curclick[1],450,500),confidence=0.75))
        elif pyautogui.locateOnScreen('Pic/spquest.png',region=(1540,468,250,200),confidence=0.75)!=None:
            pyautogui.click(pyautogui.locateOnScreen('Pic/spquest.png',region=(1540,468,250,200),confidence=0.75))
        #Xeno Select Quest
        elif pyautogui.locateOnScreen('Pic/event/Xeno/Ifrit/IfritLoop.png',region=(1414,350,470,608),confidence=0.85)!=None:         
            pos = pyautogui.locateOnScreen('Pic/event/Xeno/Ifrit/IfritLoop.png',region=(1414,350,470,608),confidence=0.85)
            pyautogui.click(pyautogui.locateOnScreen('Pic/playevent.png',region=(pos[0],pos[1],500,300),confidence=0.85))
            SelectQuest = True 
        elif pyautogui.locateOnScreen('Pic/event/Xeno/Ifrit/IfritClash.png',region=(1414,387,470,608),confidence=0.9)!=None:
            if SelectQuest == True:
                pos = pyautogui.locateOnScreen('Pic/event/Xeno/Ifrit/IfritClash.png',region=(1414,387,470,608),confidence=0.9)
                pyautogui.click(pyautogui.locateOnScreen('Pic/selectquest.png',region=(pos[0],pos[1],400,200),confidence=0.8))
                SelectQuest = False
        elif pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,300,200),confidence=0.95)!=None: #Play Againbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            print("Play Again")
            Function.Finish_PLAYAGAIN(pyautogui.locateOnScreen('Pic/playagain.png',region=(1409,509,300,200),confidence=0.95))
        elif pyautogui.locateOnScreen('Pic/skyscope.png',region=(1526,318,300,200),confidence=0.9)!=None: #Play Againbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            print("Skyscope")
            pyautogui.click(pyautogui.locateOnScreen('Pic/closehalo.png',region=(1500,650,300,400),confidence=0.75))
        
       # else:    
        #    print("--- %s seconds ---" % (time.time() - start_time))

    except Exception as e:
        #play = False
        print(e)




