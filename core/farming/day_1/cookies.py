from utils.driver import close_all_windows_driver

from utils.driver import search_and_click_to_site
from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.google import auth_google

import time
def cookies(driver):
    '''Нагуливаем куки на гигантах'''
    # close_all_windows_driver(driver)
    canvas(driver)
    
    search_and_click_to_site(driver, 'amazon+buy+books', 'www.amazon.com')
    
    
    
    
    
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
    
    
    
    
    