import pyautogui, time, traceback  
from coinmarketcap_filter_func import * 

# ============================== Configuration =============================== 
pyautogui.FAILSAFE=False 

# Only one can be true (used as selection) 
ONEHR_REFRESH_FLAG=False 
TWENTYFOURHR_REFRESH_FLAG=True 

LOG_FILE="log.txt" 
INTERVAL=60 # seconds between each refresh 

""" Market prices update every 60 seconds; so we will use 60s time as the 
    reference for how frequently we want to update the XXh change. 
       
    Refresh XXhr change market (descending) every 60 seconds. """ 

# ============================ Utility Functions ============================= 

def log_error(): 
    """ Log exceptions to file with timestamps. """ 
    with open(LOG_FILE, "a") as f:
        f.write("\n=============================\n") 
        f.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        f.write(traceback.format_exc) 
        f.write("\n") 

def focus_browser():
    """ Bring browser window into focus before interacting. """  
    pyautogui.click(Browser.x, Browser.y) 
    time.sleep(SLEEP_TIME_FAST) 

# ============================= Main Routine ================================= 

def Run():
    print("\nCoinMarketCap filter Initiating...")

    # set up of coinmarketcap filter 
    time.sleep(SLEEP_TIME_XSLOW)        # 5 second delay for start-up time.
    focus_browser()
    pyautogui.press('F11')              # full-screen chrome browser 
    filter_startup() 
    focus_browser() 
    time.sleep(SLEEP_TIME_XSLOW)        # wait for filter to adjust  

    # initial click 
    if ONEHR_REFRESH_FLAG:
        pyautogui.click(OneHrPrcntButton.x, OneHrPrcntButton.y) 

    if TWENTYFOURHR_REFRESH_FLAG:
        pyautogui.click(TwentyFourHrPrcntButton.x, TwentyFourHrPrcntButton.y) 

    print("\nCoinMarketCap filter Running...\n")

    # ============================= Scheduler ================================  
    start_time=time.time() 
    next_run=start_time+INTERVAL 
    count=0                                 # dash counter 

    while True:
        try:
            now=time.time() 

            if now>=next_run:
                # run the refresh 
                focus_browser() 
                    
                if ONEHR_REFRESH_FLAG:
                    OneHrPrcntRefresh() 
                if TWENTYFOURHR_REFRESH_FLAG:
                    TwentyFourHrPrcntRefresh() 

                print("-", end=" ", flush=True)
                count+=1                    # increment dash count 

                next_run+=INTERVAL          # schedule next run 
            
            # sleep dynamically until next_run 
            sleep_time=next_run-time.time() 
            if sleep_time>0:
                time.sleep(sleep_time) 

        except KeyboardInterrupt: 
            # program run-time in minutes (also counts dashes from start)
            end_time=int(time.time()-start_time)//60 
            print(f"\n\nDash count: {count}")
            input(f"Program run-time: {end_time}m\nPress any key to exit...") 
            break 

        except Exception:
            # log exception and recover 
            log_error()
            print("\nRecovered from error, restarting in 5s...")
            time.sleep(SLEEP_TIME_XSLOW)    # 5s sleep before restarting 

# ================================ Entry Point =============================== 
if __name__=="__main__":
    Run() 
    