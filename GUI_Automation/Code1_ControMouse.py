import pyautogui
import time

time.sleep(1)
postion = pyautogui.position()
print(postion)

#sample file coordinate
x= 131
y=157

#pyautogui.moveTo(x,y)
# drag mouse from current position
#pyautogui.move(100,0,duration=1)

#pyautogui.click(clicks=2)
#pyautogui.doubleClick()


#by default left button
#pyautogui.click(x,y,clicks=2)
#right click on windows
#pyautogui.click(x,y,button='right')
#right clicn on MAC
#pyautogui.dragTo(x,y,button='right')


#draw on jspaint.app, open on browser and keep it on right side on the screen
pyautogui.moveTo(1326,587,duration=1)
pyautogui.click()
pyautogui.drag(150,0,button='left')
pyautogui.drag(0,-150,button='left')
pyautogui.drag(-150,0,button='left')
pyautogui.drag(0,150,button='left')