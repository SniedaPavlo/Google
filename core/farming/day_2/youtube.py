

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, switch_to_window_url, asyncClickToXpath2SecJS, asyncClickToXpath2Sec

import time
import random


def youtube_subcribe_and_like(driver):
    driver.get('https://www.youtube.com/')
    
    #! Если первый раз входим - чекаем залошинен ли аккаунт
    try:
       
        #клик на Auth
        asyncClickToXpath2SecJS(driver, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a')
        
        #клик на аккаунт 
        asyncClickToXpath2SecJS(driver, '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]/div')
        
        input_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        #ПАРОЛЬ
        input_password.send_keys('Pppp4444')
        #next btn click
        asyncClickToXpath2Sec(driver, '//*[@id="passwordNext"]/div/button')
        
        #клик skip
        asyncClickToXpath2Sec(driver, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div/div/div[4]/div[1]/button')
        
    except Exception as e:
        print('Пользователь уже залогинен! Работаем дальше. (функция youtube_subcribe_and_like)')
        
    
    #! Создание канала 
    try:
        driver.get('https://www.youtube.com/')
        #клик на аватарку
        asyncClickToXpath5Sec(driver, '//*[@id="avatar-btn"]')
        #клик на create channel
        asyncClickToXpath5Sec(driver, '//*[@id="manage-account"]/a')
        #клик на подтверждение создания канала
        asyncClickToXpath5Sec(driver, '//*[@id="create-channel-button"]/yt-button-shape/button')
    except Exception as e:
        print('Ошибка во время создания канала функция "youtube_subcribe_and_like":', e)
        
        time.sleep(5)
        
    #! Накрутка сабов, лайков и коментов
    try:
        #РЕФАКТОРИНГ линки с базы брать
        links = [
            'https://www.youtube.com/watch?v=KOgvA98FifU',
            'https://www.youtube.com/watch?v=wCtvDerllj0', 
        ]
        comments = [
            'nice', 'good!', 'very nice!'
        ]
        
        for link in links:
            driver.get(link)
            # Создаем цепочку действий
            actions = ActionChains(driver)
            # Нажимаем пробел для паузы
            actions.send_keys(Keys.SPACE)
            # Выполняем действие
            actions.perform()
            #клик на саб
            asyncClickToXpath5SecJS(driver, '//*[@id="subscribe-button-shape"]/button/yt-touch-feedback-shape/div/div[2]')
            #like click
            asyncClickToXpath2SecJS(driver, '//*[@title="I like this"]')
            # ПОКАЧТО КОМЕНТОВ НЕ БУДЕТ, ТАМ ТЯЖЕЛО ПИСАТЬ. РАЗВЕ ЧТО ФОКУС ПОЗЖЕ СДЕЛАТЬ И НА ВЫШЕ УРОВНЕ ПЕЧАТАТЬ КАК ВЫШЕ ПРОБЕЛ.
            # random_comment = random.choice(comments)
            # actions = ActionChains(driver)
            # for char in random_comment:
            #     actions.send_keys(char)
            # actions.send_keys(Keys.RETURN)
            # actions.perform()
            
        driver.get('https://mail.google.com/mail/')
    except Exception as e:
        print('Ошибка во время накрутки сабов, лайков и комент "youtube_subcribe_and_like":', e)
        
        
        
        
def youtube_subcribe_and_like_without_auth(driver):
    #! Накрутка сабов, лайков и коментов
    try:
        #РЕФАКТОРИНГ линки с базы брать
        links = [
            'https://www.youtube.com/watch?v=KOgvA98FifU',
            'https://www.youtube.com/watch?v=wCtvDerllj0', 
        ]
        comments = [
            'nice', 'good!', 'very nice!'
        ]
        
        for link in links:
            driver.get(link)
            # Создаем цепочку действий
            actions = ActionChains(driver)
            # Нажимаем пробел для паузы
            actions.send_keys(Keys.SPACE)
            # Выполняем действие
            actions.perform()
            #клик на саб
            asyncClickToXpath5SecJS(driver, '//*[@id="subscribe-button-shape"]/button/yt-touch-feedback-shape/div/div[2]')
            #like click
            asyncClickToXpath2SecJS(driver, '//*[@title="I like this"]')
            # ПОКАЧТО КОМЕНТОВ НЕ БУДЕТ, ТАМ ТЯЖЕЛО ПИСАТЬ. РАЗВЕ ЧТО ФОКУС ПОЗЖЕ СДЕЛАТЬ И НА ВЫШЕ УРОВНЕ ПЕЧАТАТЬ КАК ВЫШЕ ПРОБЕЛ.
            # random_comment = random.choice(comments)
            # actions = ActionChains(driver)
            # for char in random_comment:
            #     actions.send_keys(char)
            # actions.send_keys(Keys.RETURN)
            # actions.perform()
        driver.get('https://mail.google.com/mail/')
    except Exception as e:
        print('Ошибка во время накрутки сабов, лайков и комент "youtube_subcribe_and_like":', e)
        