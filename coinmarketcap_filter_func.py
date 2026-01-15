import pyautogui, time 
from filter_defines import *

SLEEP_TIME_BETWEEN_PRESS=0.5

## Functions ## 
def filter_startup():

     # essential filter start-up #
    pyautogui.click(FiltersButton.x, FiltersButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS)

    pyautogui.click(VisibleCoinsButton.x, VisibleCoinsButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS)

    pyautogui.click(ShowAllButton.x, ShowAllButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS)

    # crypto.com is the exchange we are focused on as that is our exchange. 
    pyautogui.click(ExchangeButton.x, ExchangeButton.y)
    pyautogui.press("c")
    pyautogui.press("r")
    pyautogui.press("y")
    time.sleep(SLEEP_TIME_BETWEEN_PRESS)

    pyautogui.click(CryptoComExchangeButton.x, CryptoComExchangeButton.y)
    time.sleep(SLEEP_TIME_BETWEEN_PRESS)

    # filter out low 24h volume coins (rug-pull potential)
    pyautogui.click(Volume24hMinButton.x, Volume24hMinButton.y)
    pyautogui.press("1")
    pyautogui.press("0")
    pyautogui.press("0")
    pyautogui.press("0")
    pyautogui.press("0")
    pyautogui.press("0")
    pyautogui.press("0")
    time.sleep(SLEEP_TIME_BETWEEN_PRESS)

    pyautogui.click(ApplyButton.x, ApplyButton.y)  
