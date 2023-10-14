import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
red = win32api.RGB(255, 0, 0) # Red
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
win = win32gui.FindWindow(None,'Granblue Fantasy - Google Chrome')
if not(win == 0):
    rect = win32gui.GetWindowRect(win)
    x = rect[0]
    y = rect[1]
    w = rect[2] 
    h = rect[3] 
    print("Window %s:" % win32gui.GetWindowText(win))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))
    
    past_coordinates = (x, y, w, h)
else:
    print('Not Found')
    
def DrawRect(Start_x,Start_y,End_x,End_y):
    width = End_x - Start_x
    height = End_y - Start_y
    
    rectan = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rectan, win32con.RDW_INVALIDATE)
    
    for x in range(width):
        win32gui.SetPixel(dc, Start_x+x, Start_y, red)
        win32gui.SetPixel(dc, Start_x+x, Start_y+height, red)
        for y in range(height):
            win32gui.SetPixel(dc, Start_x, Start_y+y, red)
            win32gui.SetPixel(dc, Start_x+width, Start_y+y, red)
       



past_coordinates = monitor
while True:
    
    #DrawRect(x+120,y+280,x+530,y+600) # popup
   #DrawRect(x+120,y+100,x+530,y+200) # Button popup
   #DrawRect(x+90,y+550,x+530,y+700) # Result Button
   #DrawRect(x+120,y+100,x+530,y+200) # Topbar
   #DrawRect(x+320,y+550,x+530,y+700)  #x+335,y+500
     DrawRect(x+120,y+450,x+530,y+900)  #x+335,y+500
  #  DrawRect(x+70,y+110,x+550,h-10) #Game Screen width 480
    
    #CHARACTER 
    #DrawRect(x+85,y+570,x+400,y+720) # Character
    #DrawRect(x+85,y+570,x+155,y+720) # Chara 1
    #DrawRect(x+165,y+570,x+235,y+720) # Chara 2
    #DrawRect(x+245,y+570,x+320,y+720) # Chara 3
    #DrawRect(x+330,y+570,x+400,y+720) # Chara 4
    
    #SKILL 
    #DrawRect(x+200,y+650,x+505,y+700) # SKILL
    #DrawRect(x+200,y+650,x+250,y+700) # SKILL 1
    #DrawRect(x+285,y+650,x+335,y+700) # SKILL 2
    #DrawRect(x+370,y+650,x+420,y+700) # SKILL 3
    #DrawRect(x+455,y+650,x+505,y+700) # SKILL 4
    
    
    #SKILL ON Character
    #DrawRect(x+180,y+330,x+440,y+650) # ALL CHARA
    #DrawRect(x+185,y+335,x+255,y+480) # ON MC
    #DrawRect(x+275,y+335,x+350,y+480) # ON 2nd Chara
    #DrawRect(x+370,y+335,x+440,y+480) # ON 3rd Chara
    #DrawRect(x+185,y+505,x+255,y+650) # ON 4th Chara
    #DrawRect(x+275,y+505,x+350,y+650) # ON 5th Chara
    #DrawRect(x+370,y+505,x+440,y+650) # ON 6th Chara
    
    
    #SUMMON
    #DrawRect(x+420,y+570,x+500,y+720) # Select Summon
    #DrawRect(x+85,y+570,x+155,y+720) # Summon1
    #DrawRect(x+160,y+570,x+230,y+720) # Summon2
    #DrawRect(x+235,y+570,x+310,y+720) # Summon3
    #DrawRect(x+315,y+570,x+385,y+720) # Summon4
    #DrawRect(x+390,y+570,x+460,y+720) # Summon5
    #DrawRect(x+470,y+570,x+540,y+720) # Summon6
    

    