import win32gui

win = win32gui.FindWindow(None,'Granblue Fantasy - Personal - Microsoft​ Edge')

if not(win == 0):
    rect = win32gui.GetWindowRect(win)
    x = rect[0]
    y = rect[1]
    w = rect[2] 
    h = rect[3] 
    print("Window %s:" % win32gui.GetWindowText(win))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))
else:
    print('Not Found')
