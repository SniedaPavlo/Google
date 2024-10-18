from utils.driver import close_all_windows_driver

from utils.driver import search_and_click_to_site
from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.google import auth_google, auth_google_current_window


from selenium.webdriver.common.by import By

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url

import time
import random



import time
def cookies(driver):
    '''Нагуливаем куки на гигантах'''
    # canvas(driver)
    
    try:
        pinterest(driver)
    except Exception as e:
        print('Ошибка в функции "cookies":', e)
        
    time.sleep(20)
    # gpt(driver)
    # search_and_click_to_site(driver, 'amazon+buy+books', 'www.amazon.com')
    
def canvas(driver):
    driver.get('https://www.canva.com/')
    
    time.sleep(5)
    #прием кук
    asyncClickToXpath5SecJS(driver, '/html/body/div[2]/div/div/div/div/div[2]/button[1]')
    #клик sing in 
    asyncClickToXpath5SecJS(driver, '//*[@id="root"]/div/div[3]/div/div[2]/div/header/div[6]/button[2]')
    #клик google
    asyncClickToXpath5SecJS(driver, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/button[1]')
    
    auth_google(driver, 'Default4444')
    
    #ТЕСТ
def gpt(driver):
    driver.get('https://chatgpt.com/')
    # click sing in
    asyncClickToXpath5SecJS(driver, '/html/body/div[1]/div/main/div[1]/div[1]/div/div[1]/div/div[3]/div/button[2]')
    #  click google
    asyncClickToXpath5SecJS(driver, '/html/body/div/main/section/div[2]/div[3]/button[1]')
    
    auth_google_current_window(driver, 'Default4444')
    
    
    
    
def pinterest(driver):
    driver.get('https://www.pinterest.com/')
    
    asyncClickToXpath5Sec(driver, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[3]/button')
    
    iframe = driver.find_element(By.XPATH, "//*[@class='S9gUrf-YoZ4jf']//iframe")
    driver.switch_to.frame(iframe)
    
    # Клик на гугл
    asyncClickToXpath5Sec(driver, '//*[@id="container"]/div')
    
    auth_google(driver, 'Default')
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    print('driver.current_url', driver.current_url)
    
    close_all_windows_driver(driver, 'https://www.pinterest.com')
    
    input_date = driver.find_element(By.XPATH, '//*[@id="birthday"]')
    input_date.send_keys('03-02-1990')
    
    asyncClickToXpath5Sec(driver, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[6]/button')
    
    try:
        asyncClickToXpath5Sec(driver, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/button')
        
        radio_female = driver.find_element(By.XPATH, '//*[@id="female"]')
        radio_female.click()
        
        asyncClickToXpath5Sec(driver, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/button')
        
        
        imgs = driver.find_elements(By.XPATH, '//*[@class="S9z eEj CCY oCZ Tbt L4E e8F BG7"]')
        imgs[0].click()
        imgs[1].click()
        imgs[2].click()
        imgs[3].click()
        imgs[4].click()
        imgs[5].click()
        asyncClickToXpath5Sec(driver, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[1]/div/div/div/div/div/div/div')
        
    except:
        pass
    
    