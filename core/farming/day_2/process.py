

from core.farming.day_2.youtube import youtube_subcribe_and_like, youtube_subcribe_and_like_without_auth
from core.farming.day_2.cookies import gemini, twitter, firebase

from core.farming.day_2.newletters import axios
def process_day_2(driver, acc, acc_path):
    #Нагуливаю куки на гигантов
    try:
        # gemini(driver)
        # axios(driver, 'iker30sepj@gmail.com')
        # twitter(driver)
        # youtube_subcribe_and_like_without_auth(driver)
        firebase(driver)
        
    except Exception as e:
        print('Ошибка в core/farming/day_2/process.py функция process_day_2:', e)