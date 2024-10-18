

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.google import auth_google_current_window 

import time
import random




# https://gemini.google.com/
# !------------gemini------------
def gemini(driver):
    driver.get('https://gemini.google.com/')
    
    #click sing in
    asyncClickToXpath5SecJS(driver, '//*[@id="gb"]/div/div[1]/a')
    
    auth_google_current_window(driver, 'Default4444')
    
    time.sleep(10)
    
    # РЕФАКТОРИНГ не работает. Палит фродка и все. Немогу зайти
    
    # # 
    # asyncClickToXpath5SecJS(driver, '//*[@id="mat-mdc-dialog-0"]/div/div/discovery-card-dialog/mat-dialog-actions/button')
    
    # asyncClickToXpath5SecJS(driver, '//*[@id="mat-mdc-dialog-0"]/div/div/discovery-card-dialog/mat-dialog-actions/button[2]')
    
    # # asyncClickToXpath5SecJS(driver, '//*[@id="app-root"]/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div[2]/chat-window/div[1]/div[2]/div[1]/input-area-v2/div/div/div[1]')
    
    # # Аля-инпут
    # editable_div = driver.find_element(By.XPATH, '//*[@class="ql-editor textarea ql-blank"]')
    # # Отправляем текст в элемент
    # editable_div.send_keys("What to name a dog")
        
    
