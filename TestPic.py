import pyautogui
import time
import Function
time.sleep(1)
attack= True
#declare Variable
play = True
checkicon = False
border = [0,0,0,0]
while play: 
    
    try:
        start_time = time.time()

        if pyautogui.locateOnScreen('Pic/gameicon.png',region=(0,0,1920,80),confidence=0.75)!=None:
            checkborder = pyautogui.locateOnScreen('Pic/gameicon.png',region=(0,0,1920,80),confidence=0.75)
            checkicon = False
            border[0]= checkborder[0]
            border[1]= checkborder[1]
            border[2]= checkborder[0]
            border[3]= 1024       
        if checkicon == False:           
            #curclick = pyautogui.locateOnScreen('Pic/closehalo.png',region=(border),confidence=0.75)
            curclick = pyautogui.locateOnScreen('Pic/ok.png',region=(1622,564,300,400),confidence=0.8)
        #+84,-139
        #pyautogui.moveTo(curclick[0],curclick[1]-200)
        pyautogui.moveTo(curclick)
        print(curclick)
       # print(pos[0:2])
       # print(pos[0]+168)
       # print(pos[1]+392)
        print("--- %s seconds ---" % (time.time() - start_time))

    except Exception as e:
        play = False
        print(e)