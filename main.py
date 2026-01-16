import pyautogui, time 
from coinmarketcap_filter_func import * 

pyautogui.FAILSAFE=True 

# only one can be true (used as selection)
ONEHR_REFRESH_FLAG=True    
TWENTYFOURHR_REFRESH_FLAG=False 

# set up of coinmarketcap filter 
time.sleep(10)                      # 10 second delay for start-up load time.

pyautogui.click(Browser.x, Browser.y)

pyautogui.press('F11')              # full-screen chrome browser 

filter_startup() 

time.sleep(3)

if ONEHR_REFRESH_FLAG:
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 

if TWENTYFOURHR_REFRESH_FLAG:
    pyautogui.click(TwentyFourHrPrcntButton.x, TwentyFourHrPrcntButton.y) 

# market prices update every 60 seconds; so we will use 30 seconds time as the 
# reference for how frequently we want to update the XXh change. 

# refresh XXhr change market (descending) every 30 seconds. 

while True:

    time.sleep(30)                  # refresh "XXh %" every 30 seconds 
    
    if ONEHR_REFRESH_FLAG:
        OneHrPrcntRefresh() 

    if TWENTYFOURHR_REFRESH_FLAG:
        TwentyFourHrPrcntRefresh() 




