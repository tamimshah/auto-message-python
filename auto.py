import pyautogui
import time
time.sleep(5)
count=0
while count<=500:
    pyautogui.typewrite("Assalamulaikum Bhai!")
    pyautogui.press("enter")
    count=count+1