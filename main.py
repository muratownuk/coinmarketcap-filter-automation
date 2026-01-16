import pyautogui, time 
from coinmarketcap_filter_func import * 
from filter_defines import OneHrPrcntButton, Browser 

pyautogui.FAILSAFE=True 
FILTER_REFRESH_FLAG=False; 
SLEEP_TIME_BETWEEN_PRESS_FAST=0.5

counter=0 

#pyautogui.displayMousePosition()


# set up of coinmarketcap filter 
time.sleep(5)                       # 30 second delay for start-up load time.

pyautogui.click(Browser.x, Browser.y)

pyautogui.press('F11')              # full-screen chrome browser 

filter_startup() 

time.sleep(3)

pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 


# market prices update every 60 seconds; so we will use that time as the 
# reference for how frequently we want to update the 1h change. 

# refresh 1hr change market (descending) every 60 seconds. 
# refresh filter every 5 min. 

while True:

    time.sleep(60)                  # refresh "1h %" every 60 seconds 
    OneHrPrcntRefresh() 
    if FILTER_REFRESH_FLAG:
        # RefreshFilter()           # need to write... 
        FILTER_REFRESH_FLAG=False

    counter=counter+1
    if counter==5: 
        FILTER_REFRESH_FLAG=True 














