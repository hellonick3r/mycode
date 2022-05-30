import pyautogui
import time
time.sleep(5)

with open('text.txt','r') as f:
    text = f.read()
    for i in range(0,10):
        pyautogui.typewrite(text)
        pyautogui.typewrite('\n')
        print(i)

