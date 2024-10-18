

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url

import time
import random




# https://gemini.google.com/
# !------------gemini------------
def gemini(driver):
    driver.get('https://gemini.google.com/')
    
    #click chat with gemini
    asyncClickToXpath5Sec(driver, '//*[@id="app-root"]/main/side-navigation-v2/mat-sidenav-container/mat-sidenav-content/div/div/welcome-window/div/landing-page-variant-a/div/div/div[2]/button')
    # 
    asyncClickToXpath5SecJS(driver, '//*[@id="mat-mdc-dialog-0"]/div/div/discovery-card-dialog/mat-dialog-actions/button')
    
    asyncClickToXpath5SecJS(driver, '//*[@id="mat-mdc-dialog-0"]/div/div/discovery-card-dialog/mat-dialog-actions/button[2]')
    
    asyncClickToXpath5SecJS(driver, '//*[@id="app-root"]/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div[2]/chat-window/div[1]/div[2]/div[1]/input-area-v2/div/div/div[1]')
    
    
    
    
    