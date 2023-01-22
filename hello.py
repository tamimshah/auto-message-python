import pyautogui
import time
time.sleep(5)
count=0
while count<=5:
    pyautogui.typewrite("Anik koi Tui?")
    pyautogui.press("enter")
    count=count+1
