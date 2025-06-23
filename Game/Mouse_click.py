#x = 738, y =780
### This will hover the mouse on the error button of the Remote Network to get the value of tunnels which are OK.(From Cloud- status)
### We will use pytesseract to extract the value from the image...


import pyautogui
import time

time.sleep(10)

pyautogui.alert("program start", 'alert')
time.sleep(3)


## This are the coordinate of hovering over the 
x1,y1 = 738, 780
pyautogui.moveTo(x1,y1, duration= 1)
# x1_1,y1_1 = 742, 480
# pyautogui.moveTo(x1_1,y1_1, duration= 1)
# pyautogui.click()
# pyautogui.moveTo(x1,y1, duration= 1)

bbox = (750, 798 ,159, 111)
image = pyautogui.screenshot(region=bbox)
image.show()
time.sleep(5)

x2,y2 = 742, 480
pyautogui.moveTo(x2,y2, duration= 1)
time.sleep(5)