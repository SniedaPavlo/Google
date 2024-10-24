
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url
from utils.json import update_json_value

import time
import random

# def auth_google(driver, password, acc_path=None, label=None):
#     # Будет трекать, что мы начинали логин
#     start_login = False
   
#     time.sleep(2)
#     windows = driver.window_handles
#     print('windows', windows)
#     time.sleep(1)

#     switch_to_window_url(driver,  'https://accounts.google.com/o/oauth2/')
        
#     time.sleep(1)
#     asyncClickToXpath5SecJS(driver, "//*[@class='VV3oRb YZVTmd SmR8']")

#     try:
#         # time.sleep(1)
#         input_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
#         input_password.send_keys(password)
        
#         #клик на next 
#         asyncClickToXpath5SecJS(driver, '//*[@id="passwordNext"]/div/button')
        
#         start_login = True
#     except Exception as e:
#         print('Нет инпута пароля при auth google. Продолжаем без него')
#     finally:
#         #клик на contuniue
#         try:
#             asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button')
#         except Exception as e:
#             print('Нет кнопки "continue" при входе гугл. Работаем без нее.')
#         finally:
#             windows = driver.window_handles
#             driver.switch_to.window(windows[0])
            
#             time.sleep(4)
            
#             # проверка, что вход был совершен и подтверждаем логин
#             if start_login and len(windows) == 1 and "accounts.google.com/o/oauth2/" not in driver.current_url:
#                 print("UPDATE")
#                 update_json_value(acc_path, label, True)
                
            
def auth_google(driver, password, acc_path=None, label=None):
    
    time.sleep(2)
    windows = driver.window_handles
    print('windows', windows)
    time.sleep(1)

    switch_to_window_url(driver, 'https://accounts.google.com/')
    
        
    time.sleep(1)
    asyncClickToXpath5SecJS(driver, "//*[@class='VV3oRb YZVTmd SmR8']")

    try:
        # Ожидание появления поля ввода пароля
        input_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
        input_password.send_keys(password)

        # Клик на next
        asyncClickToXpath5SecJS(driver, '//*[@id="passwordNext"]/div/button')
        
    except NoSuchElementException:
        print('Нет инпута пароля при auth google. Продолжаем без него.')
    except Exception as e:
        print('Ошибка при вводе пароля:', e)
    
    finally:
        # Клик на continue
        try:
            asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button')
        except NoSuchElementException:
            print('Нет кнопки "continue" при входе в Google. Работаем без нее.')
        except Exception as e:
            print('Ошибка при клике на "continue":', e)

        finally:
            windows = driver.window_handles
            driver.switch_to.window(windows[0])
            
            time.sleep(4)
            
            # print(f'start_login: {start_login}')
            # print(f'Текущий URL: {driver.current_url}')
            
            # # Проверка, что вход был совершен и подтверждаем логин
            # if start_login and "accounts.google.com/o/oauth2/" not in driver.current_url:
            #     print("UPDATE")
            #     update_json_value(acc_path, label, True)
                
    
def auth_google_current_window(driver, password, acc_path=None, label=None):
    
    asyncClickToXpath5SecJS(driver, "//*[@class='VV3oRb YZVTmd SmR8']")
    try:
        input_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        input_password.send_keys(password)
        
        # Клик на next 
        asyncClickToXpath5SecJS(driver, '//*[@id="passwordNext"]/div/button')
        
    except Exception as e:
        print('Нет инпута пароля при auth google:', str(e))
    
    finally:
        # Клик на continue
        try:
            asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button')
        except Exception as e:
            print('Нет кнопки "continue" при входе в Google:', str(e))
        
        finally:
            windows = driver.window_handles
            driver.switch_to.window(windows[0])
            
            time.sleep(4)
            
            # print(f'start_login: {start_login}')
            # print(f'Текущий URL: {driver.current_url}')
            # # Проверка, что вход был совершен и подтверждаем логин
            # if start_login and "accounts.google.com/o/oauth2/" not in driver.current_url:
            #     print("UPDATE")
            #     update_json_value(acc_path, label, True)
                
# def auth_google_current_window(driver, password, acc_path=None, label=None):
#     # Будет трекать, что мы начинали логин
#     start_login = False
    
#     asyncClickToXpath5SecJS(driver, "//*[@class='VV3oRb YZVTmd SmR8']")
#     try:
#         # time.sleep(1)
#         input_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
#         input_password.send_keys(password)
        
#         #клик на next 
#         asyncClickToXpath5SecJS(driver, '//*[@id="passwordNext"]/div/button')
        
#         start_login = True
        
#     except Exception as e:
#         print('Нет инпута пароля при auth google. Продолжаем без него')
#     finally:
#         #клик на contuniue
#         try:
#             asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button')
#         except Exception as e:
#             print('Нет кнопки "continue" при входе гугл. Работаем без нее.')
#         finally:
#             windows = driver.window_handles
#             driver.switch_to.window(windows[0])
            
#             time.sleep(4)
            
#             # проверка, что вход был совершен и подтверждаем логин
#             if start_login and len(windows) == 1 and "accounts.google.com/o/oauth2/" not in driver.current_url:
#                 print("UPDATE")
#                 update_json_value(acc_path, label, True)
            
            
#! Поиск(search google) и клик по нужному сайту 
def search_and_click_to_site(driver, search, url_consider):
    """
    Ищет сайт в Google по заданному тексту и кликает на него, если href содержит заданный текст.
    """
    try:
        driver.get(f'https://www.google.com/search?q={search}')
        
        # Проверка первого XPath
        try:
            sites = driver.find_elements(By.XPATH, "//a[@jsname='UWckNb']")
            if not sites:
                raise NoSuchElementException("Элементы с первым XPath не найдены")
        except NoSuchElementException:
            # Если элементы с первым XPath не найдены, проверяем второй XPath
            sites = driver.find_elements(By.XPATH, "//*[@class='qLRx3b tjvcx GvPZzd cHaqb']")

        for site in sites:
            href = site.get_attribute('href')
            if url_consider in href: 
                site.click()
                break
        
    except Exception as e:
        print('Ошибка в функции "search_and_click_to_site":', e)



def search_and_click_to_site_and_scroll(driver, search, url_consider):
    '''
    search = текст, который попадает в query параметры и по нему ищем.
    url_consider = текст, который сравниваем. Если href содержит этот текст — переходим на сайт.
    '''
    try:
        driver.get(f'https://www.google.com/search?q={search}')
        
        # Проверка первого XPath
        try:
            sites = driver.find_elements(By.XPATH, "//a[@jsname='UWckNb']")
            if len(sites) == 0:
                raise NoSuchElementException
        except NoSuchElementException:
            # Если элементы с первым XPath не найдены, проверяем второй XPath
            sites = driver.find_elements(By.XPATH, "//*[@class='qLRx3b tjvcx GvPZzd cHaqb']")

        for site in sites:
            href = site.get_attribute('href')
            if url_consider in href:
                site.click()
                break

        time.sleep(random.randint(10, 25))

        # Скролл вниз до конца страницы
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(random.randint(5, 10))

    except Exception as e:
        print('Ошибка в utils/driver.py функция "search_and_click_to_site_and_scroll":', e)
        
        
def google_update_key(driver, acc_path, key, service_name):
    driver.get('https://myaccount.google.com/u/2/connections')
    
    services_logged = driver.find_elements(By.XPATH, "//*[@class='mMsbvc']")
    
    for service in services_logged:
        service_text = service.text  
        if service_name in service_text:
              update_json_value(acc_path, key, True)
