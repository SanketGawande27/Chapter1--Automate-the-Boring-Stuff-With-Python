#Moving mouse pointer: square 

import pyautogui
for i in range(10): # Move mouse in a square.
    pyautogui.moveTo(100, 100, duration=0.45)
    pyautogui.moveTo(400, 400, duration=0.45)
    pyautogui.moveTo(400, 400, duration=0.45)
    pyautogui.moveTo(100, 400, duration=0.45) 
