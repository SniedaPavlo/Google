

from core.farming.day_2.youtube import youtube_create_acc, youtube_subcribe_and_like
from core.farming.day_2.cookies import cookies

from core.farming.day_2.newletters import axios
def process_day_2(driver, acc, acc_path):
    
    try:
       cookies(driver, acc, acc_path)
    except Exception as e:
        print('Ошибка в функции process_day_2 при cookies', e)
        
    if not acc['farm']['youtube_create_acc']:
        #ютуб создание акка
        try:
            youtube_create_acc(driver, acc, acc_path)
        except Exception as e:
            print('Ошибка в core/farming/day_2/process.py функция youtube_create_acc:', e)
            
    if acc['farm']['youtube_create_acc'] and not acc['farm']['youtube_subcribe_and_like']:
        #ютуб фарминг просмотров и лайков
        try:
            youtube_subcribe_and_like(driver, acc, acc_path)
        except Exception as e:
            print('Ошибка в core/farming/day_2/process.py функция youtube_subcribe_and_like:', e)
    
    if not acc['farm']['axios']:
        axios(driver, acc, acc_path)