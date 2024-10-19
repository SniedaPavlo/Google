

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.google import auth_google_current_window, auth_google

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
        
    
# РЕФАКТОРИНГ следует доделать
# !------------twitter------------
# https://x.com/
def twitter(driver):
    driver.get('https://x.com/')
    
    # Привем кук
    asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/button[1]')
    
    # Клик на гугл
    asyncClickToXpath5Sec(driver, "//*[name()='iframe']")
    
    auth_google(driver, 'Default4444')
    
    select_month = driver.find_element(By.XPATH, "//select[@aria-labelledby='SELECTOR_1_LABEL']")
    select = Select(select_month)
    options = select.options
    print('options', options)
    random_option = random.choice(options)
    # Выполняем клик на случайной опции
    select.select_by_visible_text(random_option.text)
    
    select_day = driver.find_element(By.XPATH, "//select[@aria-labelledby='SELECTOR_2_LABEL']")
    select = Select(select_day)
    options = select.options
    print('options', options)
    random_option = random.choice(options)
    # Выполняем клик на случайной опции
    select.select_by_visible_text(random_option.text)
    
    select_day = driver.find_element(By.XPATH, "//select[@aria-labelledby='SELECTOR_3_LABEL']")
    select = Select(select_day)
    options = select.options
    print('options', options)
    random_option = random.choice(options)
    # Выполняем клик на случайной опции
    select.select_by_visible_text('1999')
    
    # click sing in 
    asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    
    # РЕФАКТИНГ вход в гугл выше сделан. Но не регает аккаунт до конца
    # # skip for now
    # asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    # # 
    # asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button[2]')
    
    # btns_sub = driver.find_elements(driver, "//*[@class='css-175oi2r r-1q9bdsx r-t60dpp r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
    
    # for i in range(6):
    #     driver.execute_script('arguments[0].click();', btns_sub[i])
        
    # # click next
    # asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/button')
    # # click next
    # asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/button')
    
    
    # btns_follow = driver.find_elements(By.XPATH, "//*[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-15ysp7h r-4wgw6l r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
    
    # for i in range(6):
    #     driver.execute_script('arguments[0].click();', btns_follow[i])
    
    # asyncClickToXpath5Sec(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    
    
