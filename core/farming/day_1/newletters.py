
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec

import time

# https://www.spiegel.de/

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
        input_username.send_keys('swiss20kteam6@gmail.com')
        
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
        
    except Exception as e:
        print('Ошибка на сайте https://www.spiegel.de/ функция "spiegel":', e)
    
    
    #! Подтверждение почты 
    try:
        driver.get('https://mail.google.com/mail/')
        
        mail_box = driver.find_element(By.XPATH, "//*[text()='DER SPIEGEL']/../../../..")
        mail_box.click()
        
        ref_linkt_verify_token = driver.find_element(By.XPATH, "//*[@rel='noreferrer']")
        driver.get(ref_linkt_verify_token.get_attribute('href'))
        # asyncClickToXpath5Sec(driver, '//*[@id=":ba"]/a[1]')
        
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