import pyautogui, time 
from filter_defines import *
from defines import * 

SLEEP_TIME_BETWEEN_PRESS_FAST=0.5
SLEEP_TIME_BETWEEN_PRESS_MID=1
SLEEP_TIME_BETWEEN_PRESS_SLOW=2

VOLUME24H=True
PRICECHANGE24H=True
Vol24hMin=FiveHundredThousand

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
    pyautogui.write(str(exchanges["1"]))            # "1" is crypto.com 
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    pyautogui.click(CryptoComExchangeButton.x, CryptoComExchangeButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    # filter out negative % 24h volume coins 
    if PRICECHANGE24H:
        pyautogui.click(PriceChange24hMinButton.x, PriceChange24hMinButton.y)
        pyautogui.write(str(3)) # filter in 3% and up 
        time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST) 

    # filter out low 24h volume coins (rug-pull potential)
    if VOLUME24H:
        pyautogui.click(Volume24hMinButton.x, Volume24hMinButton.y)
        pyautogui.write(str(Vol24hMin))
        time.sleep(SLEEP_TIME_BETWEEN_PRESS_FAST)

    pyautogui.click(ApplyButton.x, ApplyButton.y)  

def OneHrPrcntRefresh():
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_SLOW)
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_SLOW) 
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 

def TwentyFourHrPrcntRefresh():
    pyautogui.click(TwentyFourHrPrcntButton.x, TwentyFourHrPrcntButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_SLOW)
    pyautogui.click(TwentyFourHrPrcntButton.x, TwentyFourHrPrcntButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS_SLOW)
    pyautogui.click(TwentyFourHrPrcntButton.x, TwentyFourHrPrcntButton.y)

