



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.google import auth_google_current_window 
from utils.json import update_json_value

import time
import random

# ! --------axios----------
# https://www.axios.com/newsletters
def axios(driver, acc, acc_path):
    driver.get('https://www.axios.com/newsletters')
    
    asyncClickToXpath5Sec(driver, '//*[@id="__next"]/div[1]/div[2]/div[2]/header/nav/div[1]/button')
    # ckick sing in google
    asyncClickToXpath5Sec(driver, '//*[@id="google-auth-event"]/button')
    
    auth_google_current_window(driver, acc['info']['password'])
    
    btns_sub = driver.find_elements(By.XPATH, '//*[@class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer gtmClick"]')
    
    for btn in btns_sub:
        driver.execute_script('arguments[0].click();', btn)
        
    update_json_value(acc_path, 'axios', True)
    
    # РЕФАКТОРИНГ 
    input_email = driver.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys(acc['info']['gmail'])
    
    asyncClickToXpath5Sec(driver, '//*[@id="main-content"]/div/div[3]/div/div/div/form/div[3]/button')
    
    