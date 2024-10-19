

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url

import time
import random



def post_info_profile(driver, acc_path):
    driver.get('https://myaccount.google.com/personal-info?')
    #клик на гендер
    asyncClickToXpath5SecJS(driver, ' //*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[2]/div/div/div[5]/div[2]/a')
    gender = None
    radio_male = driver.find_element(By.XPATH, '//*[@id="c13"]')
    if radio_male.is_selected():
        gender = 'male'
    else:
        gender = 'famele'
    print('gender', gender)
    driver.get('https://myaccount.google.com/personal-info?')
    asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[2]/div/div/div[2]/button/div/div/div[2]/figure')
    time.sleep(3)
    # actions = ActionChains(driver)
    # element = driver.find_element(driver, '//*[@id="yDmH0d"]/c-wiz/main/div/div[2]/div')
    
    # actions.move_to_element(element).click(element).perform()
    
    asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz[2]/main[1]/div[1]/div[1]/div[2]/img[1]')
    
    asyncClickToXpath5SecJS(driver, '//*[@id="nTuXNc"]')
    # asyncClickToXpath5SecJS(driver, '//*[@id="yDmH0d"]/c-wiz/main/div/div[2]/div/div/button')
    
    
    # Список элементов для тестирования
    elements = []

    # Поиск по различным возможным атрибутам
    try:
        elements.append(driver.find_element(By.XPATH, '//*[@class="FOBRw-LgbsSe"]'))
    except:
        pass

    try:
        elements.append(driver.find_element(By.XPATH, '//*[@jscontroller="O626Fe"]'))
    except:
        pass

    try:
        elements.append(driver.find_element(By.XPATH, '//*[@jsname="NBieKd"]'))
    except:
        pass

    try:
        elements.append(driver.find_element(By.XPATH, '//*[@jsaction="click:h5M12e; clickmod:h5M12e;pointerdown:FEiYhc;pointerup:mF5Elf;"]'))
    except:
        pass

    # Пробуем отправить файл во все элементы
    file_path = "/Users/mac/Desktop/desktop/Google/data/images/gender/males/2.jpg"

    for element in elements:
        try:
            element.send_keys(file_path)
            print(f"Успешно отправлен файл в элемент: {element}")
        except Exception as e:
            print(f"Не удалось отправить файл в элемент: {element}. Ошибка: {e}")

    
    