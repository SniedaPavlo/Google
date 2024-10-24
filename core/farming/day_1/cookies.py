from utils.driver import close_all_windows_driver

from utils.google import search_and_click_to_site, search_and_click_to_site_and_scroll
from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.google import auth_google, auth_google_current_window, google_update_key
from utils.json import update_json_value

from selenium.webdriver.common.by import By

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url

import time
import random


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def cookies(driver, acc, acc_path):
    '''Нагуливаем куки на гигантах'''
    # canva
    if not acc['farm']['canva']:
        try:
            canvas(driver, acc_path)
        except Exception as e:
            print('Ошибка в функции cookies при регистрации canva', e)
    # pinterest
    if not acc['farm']['pinterest']:
        try:
            pinterest(driver, acc_path)
        except Exception as e:
            print('Ошибка в функции cookies при регистрации pinterest', e)
    # farm
    if not acc['farm']['search_cookies']:
        try:
            search_and_click_to_site_and_scroll(driver, 'amazon+buy+books', 'www.amazon.com')
            search_and_click_to_site_and_scroll(driver, 'facebook', 'facebook.com')
            search_and_click_to_site_and_scroll(driver, 'yahoo', 'www.yahoo.com')
            search_and_click_to_site_and_scroll(driver, 'Twitter', 'x.com')
        except Exception as e:
            print('Ошибка при нагуле кук 1 день')
    # gpt
    # if not acc['farm']['gpt']:
    #     try:
    #         gpt(driver, acc_path)
    #     except Exception as e:
    #         print('Ошибка в функции cookies при регистрации gpt', e)
            
    print('')
    
def canvas(driver, acc_path):
    try:
        search_and_click_to_site(driver, 'canva', 'canva.com')
        
        # driver.get('https://www.canva.com/')
        
        time.sleep(5)
        #прием кук
        asyncClickToXpath5SecJS(driver, '/html/body/div[2]/div/div/div/div/div[2]/button[1]')
        #клик sing in 
        asyncClickToXpath5SecJS(driver, '//*[@id="root"]/div/div[3]/div/div[2]/div/header/div[6]/button[2]')
        #клик google
        asyncClickToXpath5SecJS(driver, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/button[1]')
        
        auth_google(driver, 'Default4444',acc_path, 'canvas')
        
        # update_json_value(acc_path, 'canvas', True)
    except Exception as e:
        print('Ошибка во время логирования canva:', e)
    finally:
        google_update_key(driver, acc_path, 'canva', 'Canva')
        
    
    #ТЕСТ / РЕФАКТОРИНГ - он вообще не работает что-то
def gpt(driver, acc_path):
    
    try:
        search_and_click_to_site(driver, 'chatgpt', 'chatgpt.com')
        
        # driver.get('https://chatgpt.com/')
        
        # click sing in
        asyncClickToXpath5SecJS(driver, '/html/body/div[1]/div/main/div[1]/div[1]/div/div[1]/div/div[3]/div/button[2]')
        #  click google
        asyncClickToXpath5SecJS(driver, '/html/body/div/main/section/div[2]/div[3]/button[1]')
        
        auth_google_current_window(driver, 'Default4444')
        
        # time.sleep(500)
        
    except Exception as e:
        print('Ошибка при регистрации gpt:', e)
    finally:
        google_update_key(driver, acc_path, 'gpt', 'OpenAI')
    
    
    # update_json_value(acc_path, 'gpt', True)
    
    
# ! pinterest 
def pinterest(driver, acc_path):
    
    try:
        # search_and_click_to_site(driver, 'pinterest', 'www.pinterest.com')
        driver.get('https://www.pinterest.com/')
        
        time.sleep(1)

        asyncClickToXpath5SecJS(driver, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[3]/button')
        
        time.sleep(2)
        
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='S9gUrf-YoZ4jf']//iframe"))
        )
        driver.switch_to.frame(iframe)
        
        # Клик на гугл
        asyncClickToXpath5Sec(driver, '//*[@id="container"]/div')
        
        auth_google(driver, 'Default')
        
        close_all_windows_driver(driver, 'pinterest.com')
        
        input_date = driver.find_element(By.XPATH, '//*[@id="birthday"]')
        input_date.send_keys('03-02-1990')
        
        asyncClickToXpath5Sec(driver, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[6]/button')
    except Exception as e:
        print('Ошибка во время регитстрации pinterest', e)
    # РЕФАКТОРИНГ до кода ниже не дохидит
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
        
        # update_json_value(acc_path, 'pinterest', True)
        
        asyncClickToXpath5Sec(driver, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div[4]/div[2]/button')
        
        time.sleep(15)
    except:
        pass
    finally:
        google_update_key(driver, acc_path, 'pinterest', 'Pinterest')

        
    
    