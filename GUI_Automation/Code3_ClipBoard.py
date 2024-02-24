import pyautogui
import pyperclip
import time


position  = pyautogui.position()
print(position)

x= 110
y=118
#pyautogui.doubleClick(x,y)
pyautogui.click(x,y,clicks=2)
time.sleep(1)

pyautogui.hotkey('command','a')
pyautogui.hotkey('command','c')


text = pyperclip.paste()
print(text)
