from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from data.config import DONT_CLOSE_WINDOW_URL

import time


def close_all_windows_driver(driver):
    try:
        all_windows = driver.window_handles
        time.sleep(1)
        
        if len(all_windows) > 0:
            # Перебираем все окна
            for window in all_windows:
                try:
                    driver.switch_to.window(window)
                    current_url = driver.current_url

                    # Если URL не содержит DONT_CLOSE_WINDOW_URL, закрываем окно
                    if DONT_CLOSE_WINDOW_URL not in current_url:
                        driver.close()
                    
                    # Обновляем список окон после закрытия
                    all_windows = driver.window_handles
                    
                except Exception as e:
                    print(f"Ошибка: {e}, окно уже закрыто или недоступно")
            
        # Обновляем список окон и переключаемся на первое оставшееся окно
        all_windows = driver.window_handles
        if len(all_windows) > 0:
            driver.switch_to.window(all_windows[0])
    
    except Exception as e:
        print(f"Ошибка при переключении на первое окно: {e}")
            
            
#! Поиск(search google) и клик по нужному сайту 
def search_and_click_to_site(driver, search, url_consider):
    '''
    search = текст который в квери параметры попадает и ищем по нему
    url_consider = текст, который сравнимваем если содержит href сайта - переходим по нему.
    '''
    close_all_windows_driver(driver)
    
    try:
        
        driver.execute_script("window.open('https://www.google.com', 'new_window')")
        time.sleep(2)
        driver.get(f'https://www.google.com/search?q={search}')
        
        sites = driver.find_elements(By.XPATH, "//a[@jsname='UWckNb']")
        for site in sites:
            href = site.get_attribute('href')
            if url_consider in href: 
                site.click()
                break
        
    except Exception as e:
        print('Ошибка в utils/driver.py функция "sarch_and_click_to_site":', e)
        
        
        
#! Асинхзронный клик по элементу с ожиданием 5 секунд
def asyncClickToXpath5Sec(driver, xpath):
    try:
        btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print('cliked to element:', btn)
        btn.click()
    except Exception as e:
        print(f'Ошибка в функции "asyncClickToXpath5Sec" не удалось кликнуть по xpath {xpath}', e)
        
def asyncClickToXpath5SecJS(driver, xpath):
    try:
        btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print('cliked JS to element:', btn)
        driver.execute_script("arguments[0].click();", btn)
    except Exception as e:
        print(f'Ошибка в функции "asyncClickToXpath5Sec" не удалось кликнуть по xpath {xpath}', e)
        
# ! Переключает на окно котороое содержит нужный URL
def switch_to_window_url(driver, url):
    
    windows = windows = driver.window_handles
    
    # Перебираем окна
    for window in windows:
        # Переключаемся на окно
        driver.switch_to.window(window)
        
        # Получаем текущий URL
        current_url = driver.current_url
        
        # Проверяем, содержит ли URL
        if url in current_url:
            print(f"Нашли нужное окно с URL: {current_url}")
            break