
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url

import time

def auth_google(driver, password):
   
    time.sleep(2)
    windows = driver.window_handles
    print('windows', windows)
    time.sleep(1)

    switch_to_window_url(driver,  'https://accounts.google.com/o/oauth2/')
        
    time.sleep(1)
    asyncClickToXpath5SecJS(driver, "//*[@class='VV3oRb YZVTmd SmR8']")

    try:
        # time.sleep(1)
        input_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        input_password.send_keys(password)
        
        #клик на next 
        asyncClickToXpath5SecJS(driver, '//*[@id="passwordNext"]/div/button')
    except Exception as e:
        print('Нет инпута пароля при auth google. Продолжаем без него')
        
    #клик на contuniue
    time.sleep(2)
    asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button')
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    