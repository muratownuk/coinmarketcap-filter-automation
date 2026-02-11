import pyautogui, time 
from coinmarketcap_filter_func import * 

pyautogui.FAILSAFE=True 

# only one can be true (used as selection)
ONEHR_REFRESH_FLAG=False    
TWENTYFOURHR_REFRESH_FLAG=True 

# set up of coinmarketcap filter 
time.sleep(5)                       # 5 second delay for start-up load time.

print("\nCoinMarketCap filter Initiating...")

pyautogui.click(Browser.x, Browser.y)

pyautogui.press('F11')              # full-screen chrome browser 

filter_startup() 

time.sleep(7.5)                     # wait for filter to adjust (7.5s) 

if ONEHR_REFRESH_FLAG:
    pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 

if TWENTYFOURHR_REFRESH_FLAG:
    pyautogui.click(TwentyFourHrPrcntButton.x, TwentyFourHrPrcntButton.y) 

# market prices update every 60 seconds; so we will use 60 seconds time as the 
# reference for how frequently we want to update the XXh change. 

# refresh XXhr change market (descending) every 60 seconds. 

print("\nCoinMarketCap filter Running...\n") 

start_time=time.time() 
count=0                             # dash counter 

try: 
    while True:

        time.sleep(60)              # refresh "XXh %" every 60 seconds 
        
        if ONEHR_REFRESH_FLAG:
            OneHrPrcntRefresh() 

        if TWENTYFOURHR_REFRESH_FLAG:
            TwentyFourHrPrcntRefresh() 

        print("-", end=" ", flush=True)
        count+=1                    # increment dash count 

except KeyboardInterrupt: 
    # Program run-time in minutes (also counts dashes from start)
    end_time=int(time.time()-start_time)//60 
    print(f"\n\nDash count: {count}")
    input(f"Program run-time {end_time} min.\nPress any key to exit...") 
