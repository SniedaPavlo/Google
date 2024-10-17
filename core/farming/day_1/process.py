from utils.driver import close_all_windows_driver
from core.farming.day_1.newletters import spiegel, google_alerts, cheshire, theguardian

from core.farming.day_1.cookies import cookies

def process_day_1(driver):
    #Нагуливаю куки на гигантов
    try:
        theguardian(driver)
    except Exception as e:
        print('Ошибка в core/farming/day_1/process.py функция process_day_1:', e)
    
    # google_alerts(driver)
    # spiegel(driver)
    # cookies(driver)
    # cheshire(driver)