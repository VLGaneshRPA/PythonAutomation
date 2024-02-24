import pyautogui
import time


position  = pyautogui.position()
print(position)

x= 110
y=118
#pyautogui.doubleClick(x,y)
pyautogui.click(x,y,clicks=2)
time.sleep(1)

#hanged on mac
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('Indeed, Python is amazing!')


pyautogui.hotkey('command','a')
pyautogui.hotkey('command','c')
pyautogui.press(5*['down'])
pyautogui.hotkey('command','v')