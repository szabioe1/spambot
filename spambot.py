import pyautogui, time 
import os
time.sleep(5)
os.chdir(r'') #Your directory
f = open("") #Your .TXT File

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")