

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.driver import asyncClickToXpath5Sec, asyncClickToXpath5SecJS, asyncClickToXpath2SecJS,  switch_to_window_url

import time
import random



def post_info_profile(driver):
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