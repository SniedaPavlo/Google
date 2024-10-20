from utils.driver import close_all_windows_driver
from core.farming.day_1.newletters import spiegel, google_alerts, cheshire, theguardian, google_news_subscribe

from core.farming.day_1.cookies import cookies
from core.farming.day_1.post_info_profile import post_info_profile


def process_day_1(driver, acc, acc_path):
    print('process_day_1', process_day_1)
    #Нагуливаю куки на гигантов
    
    try:
       cookies(driver, acc, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при cookies ')
        
    try:
        post_info_profile(driver, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при post_info_profile', e)
    
    try:
        google_alerts(driver, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при google_alerts', e)

    try:
        spiegel(driver, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при spiegel', e)

    try:
        cheshire(driver, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при cheshire', e)
    
    try:
        theguardian(driver, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при theguardian', e)
    
    try:
        google_news_subscribe(driver, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_1 при google_news_subscribe', e)
    
