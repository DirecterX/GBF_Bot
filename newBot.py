import pyautogui
import time
import pygetwindow
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)



gameScreen = pygetwindow.getWindowsWithTitle("Granblue Fantasy - Google Chrome")[0]

x = gameScreen.left
y = gameScreen.top
w = gameScreen.width
h = gameScreen.height

print(x , y , w , h)