
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS

import time
import random

# https://www.spiegel.de/
# ! --------spiegel-------
def spiegel(driver):
    driver.get('https://www.spiegel.de/')
    
    #! Если есть модалка - сработает. Следует принять куки
    try:
        iframe = driver.find_element(By.XPATH, "//*[@id='sp_message_iframe_1181842']")
        driver.switch_to.frame(iframe)
        asyncClickToXpath5Sec(driver, "//*[@title='Consent and continue']")
    except Exception as e:
        print('Модального окна нет на сайте https://www.spiegel.de/')
    
    #! Рег аккаунта
    try:
        driver.get('https://www.spiegel.de/fuermich/')
        
        #клик на кнопку рега акка
        asyncClickToXpath5Sec(driver, '//*[@id="Inhalt"]/div[1]/div/div[2]/div[1]/a[2]')
        
        input_username = driver.find_element(By.XPATH, "//*[@id='username']")
        input_username.send_keys('panificadoracentralnobres42@gmail.com')
        
        #клика на кнопку next 
        asyncClickToXpath5Sec(driver, '//*[@id="submit"]')
        time.sleep(2)
        
        input_password = driver.find_element(By.XPATH, "//*[@id='password']")
        input_password.send_keys('Pppp4444')
        time.sleep(2)
        
        asyncClickToXpath5Sec(driver, '//*[@id="submit"]')
        time.sleep(2)
        
        asyncClickToXpath5Sec(driver, '//*[@id="acceptedTermsOfUse"]')
        time.sleep(2)
        asyncClickToXpath5Sec(driver, '//*[@id="acceptedAdvertising"]')
        time.sleep(2)
        
        #клик по кнопке submit
        asyncClickToXpath5Sec(driver, '//*[@id="submit"]')
        time.sleep(2)
        
        #----Наступная страница------
        asyncClickToXpath5Sec(driver, '//*[@id="salutation"]/div[1]/label')
        input_vorname = driver.find_element(By.XPATH, '//*[@id="givenname"]')
        input_vorname.send_keys('tetsnamee3999')
        
        input_hachname = driver.find_element(By.XPATH, '//*[@id="surname"]')
        input_hachname.send_keys('tetsnamee99')
        
        input_tt = driver.find_element(By.XPATH, '//*[@id="birthDay"]')
        input_tt.send_keys('11')
        
        input_mm = driver.find_element(By.XPATH, '//*[@id="birthMonth"]')
        input_mm.send_keys('03')
        
        input_year = driver.find_element(By.XPATH, '//*[@id="birthYear"]')
        input_year.send_keys('1998')
        
        #клик на некст
        asyncClickToXpath5Sec(driver, '//*[@id="submit"]')
        time.sleep(2)
        
    except Exception as e:
        print('Ошибка на сайте https://www.spiegel.de/ функция "spiegel":', e)
    
    
    #! Подтверждение почты 
    try:
        driver.get('https://mail.google.com/mail/')
        time.sleep(8)
        
        mail_box = driver.find_element(By.XPATH, "//*[text()='DER SPIEGEL']/../../../..")
        mail_box.click()
        
        ref_linkt_verify_token = driver.find_element(By.XPATH, "//*[@rel='noreferrer']")
        driver.get(ref_linkt_verify_token.get_attribute('href'))
        
        time.sleep(4)
        driver.get('https://www.spiegel.de/newsletter')
        
    except Exception as e:
        print('Ошибка при подтверждении email:', e)
        
    #! Подписки
    try:
        driver.get('https://www.spiegel.de/newsletter')
        #Если есть модалка - сработает. Следует принять куки
        iframe = driver.find_element(By.XPATH, '//*[@id="Inhalt"]/div[3]/div/div[1]/iframe')
        driver.switch_to.frame(iframe)
        btns_news = driver.find_elements(By.XPATH, "//*[@class='cms-button-21 small']")
        count = len(btns_news) - 2
        driver.execute_script("arguments[0].click();", btns_news[0])
        
        for i in range(count):
            
            driver.get('https://www.spiegel.de/newsletter')
            iframe = driver.find_element(By.XPATH, '//*[@id="Inhalt"]/div[3]/div/div[1]/iframe')
            driver.switch_to.frame(iframe)
            btns_news = driver.find_elements(By.XPATH, "//*[@class='cms-button-21 small']")
            driver.execute_script("arguments[0].click();", btns_news[i])
            
    except:
        print('Ошибка при нажатии на кнопки newsletter')
        
        
        
        
# !-------- google alerts ------
# https://www.google.com/alerts
def google_alerts(driver):
    
    popular_words = [
        "Sport", "Technology", "AI", "Climate Change", "Music",
        "Space Exploration", "Travel", "Photography", "Food", 
        "Gaming", "Fashion", "Mental Health", "Innovation", 
        "Finance", "Entrepreneurship", "Health", "Movies", 
        "Art", "Education", "Nature"
    ]
    
    # Генерация нового списка от 12 до 16 случайных элементов
    random_selection = random.sample(popular_words, random.randint(12, 16))

    driver.get('https://www.google.com/alerts')
    try:
        #клик по первой кнопке
        asyncClickToXpath5Sec(driver, '//*[@id="gb-main"]/div[2]/div[2]/div/div[5]/div[1]/div/div/div/div[1]/div/div/div[2]/span[1]')
        #клик по второй кнопке
        asyncClickToXpath5Sec(driver, '//*[@id="gb-main"]/div[2]/div[2]/div/div[5]/div[1]/div/div/div/div[2]/div/div/div[2]/span[1]')
    except Exception as e:
        print('Нет стартовых кнопок на https://www.google.com/alerts. Ошибка в функции "google_alerts":', e)
    
    input_search = driver.find_element(By.XPATH, '//*[@id="query_div"]/input')
        
    for char in random_selection:
        input_search.click()
        input_search.clear()
        time.sleep(1)
        input_search.send_keys(char)
        input_search.send_keys(Keys.RETURN)
        time.sleep(1)
        # Добавляем
        asyncClickToXpath5Sec(driver, '//*[@id="create_alert"]')
        
    
    
    
#! -------cheshire---------
# https://www.cheshire-live.co.uk/
def cheshire(driver):
    driver.get('https://www.cheshire-live.co.uk/')
    
    #Клик на модальное окно
    try:
        asyncClickToXpath5Sec(driver, '//*[@id="CIPAConsentNotice"]/div/div[3]/button')
    except Exception as e:
        print('Нет модального окна на сайте https://www.cheshire-live.co.uk/ функция "cheshire":', e)
        
    #клик на иконку профиля
    asyncClickToXpath5SecJS(driver, '/html/body/header/div[1]/profile-icon')
    #клик на вход по гугл
    asyncClickToXpath5SecJS(driver, "//*[@class='auth-ui-social__button auth-ui-social__button--google']")
    
    time.sleep(2)
    windows = driver.window_handles
    print('windows', windows)
    time.sleep(3)
    
    # driver.switch_to.window(windows[1])
    # print('driver.switch_to.window(windows[1])', driver.current_url)  # Получаем URL для окна 1
    # driver.switch_to.window(windows[0])
    # print('driver.switch_to.window(windows[0])', driver.current_url) 
    
    # Перебираем окна
    for window in windows:
        # Переключаемся на окно
        driver.switch_to.window(window)
        
        # Получаем текущий URL
        current_url = driver.current_url
        
        # Проверяем, содержит ли URL 'https://accounts.google.com/o/oauth2/'
        if 'https://accounts.google.com/o/oauth2/' in current_url:
            print(f"Нашли нужное окно с URL: {current_url}")
            break
        
    time.sleep(1)
    asyncClickToXpath5SecJS(driver, "//*[@class='VV3oRb YZVTmd SmR8']")

    try:
        # time.sleep(1)
        input_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        input_password.send_keys('Default4444')
        
        #клик на next 
        asyncClickToXpath5SecJS(driver, '//*[@id="passwordNext"]/div/button')
    except Exception as e:
        print('Нет инпута пароля при auth google. Продолжаем без него')
        
    #клик на contuniue
    time.sleep(2)
    asyncClickToXpath5SecJS(driver, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc LQeN7 BqKGqe pIzcPc TrZEUc lw1w4b']")
    
    
    