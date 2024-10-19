from logo_api.LocalRestAPI.open_profile_by_id import  open_profile_by_id
from logo_api.LocalRestAPI.stop_profile_by_id import stop_profile_by_id

from core.farming.day_1.process import process_day_1
from core.farming.day_2.process import process_day_2

from utils.json import load_json
from utils.os import list_files_in_directory
from utils.other import calculate_days_difference

import threading
import time
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def worker(acc_path):
    """
    Функция, выполняемая в каждом потоке.
    Здесь можно добавить любую логику, которая должна выполняться параллельно для каждого элемента списка.
    """
    try:
        acc_path = f'data/accounts/google/farm/{acc_path}'
        acc = load_json(acc_path)
        
        print('acc', acc)
        
        start_date = acc['info']['start_date']
        
        now = datetime.now()
        current_date = now.date()
        # Разница между началом (стартом фарма) и сегоднешнем днем
        days_difference = calculate_days_difference(current_date, start_date)
        
        driver_data = open_profile_by_id(acc['info']['id'], '/Users/mac/Desktop/desktop/scanner/chromedriver/chromedriver-127')
        if days_difference < 1:
            process_day_1(driver_data['driver'], acc, acc_path)
        if days_difference < 2:
            process_day_2(driver_data['driver'], acc, acc_path)
    
        print('days_difference', days_difference)
        
    except Exception as e:
        print('Error', e)
        
def create_threads(accs, max_workers=2):
    """
    Создает и запускает потоки для каждого элемента в списке.

    :param accs: Список элементов для обработки.
    :param max_workers: Максимальное количество потоков.
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(worker, accs)

# Пример использования
if __name__ == "__main__":
    # Пример списка с несколькими элементами
    accs = list_files_in_directory('data/accounts/google/farm')
    create_threads(accs, max_workers=2)