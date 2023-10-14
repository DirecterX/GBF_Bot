import pyautogui
import time
time.sleep(1)
#declare Variable
play = True
border = [600,0,1320,755]
while play: 
    
    try:
        start_time = time.time()
        #--------------------Start Stage---------------------------
        if pyautogui.locateOnScreen('arknight/start.png',region=(border),confidence=0.9)!=None:               
            pyautogui.click(pyautogui.locateOnScreen('arknight/start.png',region=(border),confidence=0.9))
            print("Stage Selected")
            time.sleep(1)
        elif pyautogui.locateOnScreen('arknight/obstart.png',region=(border),confidence=0.9)!=None:               
            pyautogui.click(pyautogui.locateOnScreen('arknight/obstart.png',region=(border),confidence=0.9))
            print("Stage Selected")
            time.sleep(1)
        elif pyautogui.locateOnScreen('arknight/cnstart.png',region=(border),confidence=0.9)!=None:               
            pyautogui.click(pyautogui.locateOnScreen('arknight/cnstart.png',region=(border),confidence=0.9))
            print("Stage Selected")
            time.sleep(1)    
        #-------------------Start Mission--------------------------    
        elif pyautogui.locateOnScreen('arknight/msstart.png',region=(border),confidence=0.9)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/msstart.png',region=(border),confidence=0.9))
            print("Start Mission")
            time.sleep(5)
        elif pyautogui.locateOnScreen('arknight/cnmsstart.png',region=(border),confidence=0.9)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/cnmsstart.png',region=(border),confidence=0.9))
            print("Start Mission")
            time.sleep(5)
        #---------------------Stage Select-------------------------
        elif pyautogui.locateOnScreen('arknight/stage.png',region=(border),confidence=0.94)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/stage.png',region=(border),confidence=0.94))
            print("Select Stage")
            time.sleep(1)
        elif pyautogui.locateOnScreen('arknight/off4.png',region=(border),confidence=0.94)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/off4.png',region=(border),confidence=0.94))
            print("Select Stage")
            time.sleep(1)
        #----------------------End Stage---------------------------        
        elif pyautogui.locateOnScreen('arknight/result.png',region=(border),confidence=0.9)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/result.png',region=(border),confidence=0.9))
            print("End Stage")
            time.sleep(1)
        elif pyautogui.locateOnScreen('arknight/cnresult.png',region=(border),confidence=0.9)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/cnresult.png',region=(border),confidence=0.9))
            print("End Stage")
            time.sleep(1)
        #----------------------Doctar Level Up---------------------------   
        elif pyautogui.locateOnScreen('arknight/levelup.png',region=(border),confidence=0.9)!=None:              
            pyautogui.click(pyautogui.locateOnScreen('arknight/levelup.png',region=(border),confidence=0.9))
            print("Doctar Level Up")
            time.sleep(1)                   
      

    except Exception as e:
        play = False
        print(e)




