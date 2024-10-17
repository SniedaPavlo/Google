

from core.farming.day_2.youtube import youtube_subcribe_and_like, youtube_subcribe_and_like_without_auth

def process_day_2(driver):
    #Нагуливаю куки на гигантов
    try:
        youtube_subcribe_and_like_without_auth(driver)
        
    except Exception as e:
        print('Ошибка в core/farming/day_2/process.py функция process_day_2:', e)