import pyautogui, time 
from coinmarketcap_filter_func import * 

pyautogui.FAILSAFE=True 
SLEEP_TIME_BETWEEN_PRESS=0.5

#pyautogui.displayMousePosition()


# set up of coinmarketcap filter 
time.sleep(5)                       # 30 second delay for start-up load time.

pyautogui.press('F11')              # full-screen chrome browser 

filter_startup() 




