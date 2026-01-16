import pyautogui, time 
from filter_defines import *

SLEEP_TIME_BETWEEN_PRESS_FAST=0.5
SLEEP_TIME_BETWEEN_PRESS_MID=1
SLEEP_TIME_BETWEEN_PRESS_SLOW=2

## Functions ## 
def filter_startup():

     # essential filter start-up #
    pyautogui.click(FiltersButton.x, FiltersButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    pyautogui.click(VisibleCoinsButton.x, VisibleCoinsButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    pyautogui.click(ShowAllButton.x, ShowAllButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    # crypto.com is the exchange we are focused on as that is our exchange. 
    pyautogui.click(ExchangeButton.x, ExchangeButton.y)
    pyautogui.write("cry")
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    pyautogui.click(CryptoComExchangeButton.x, CryptoComExchangeButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    # filter out low 24h volume coins (rug-pull potential)
    pyautogui.click(Volume24hMinButton.x, Volume24hMinButton.y)
    pyautogui.write("1000000")
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    pyautogui.click(ApplyButton.x, ApplyButton.y)  

def OneHrPrcntRefresh():
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_MID)
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_MID) 
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 


