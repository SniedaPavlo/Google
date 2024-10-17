from octo_api.profiles.get_profiles import get_profiles
from octo_api.profiles.create_profile import create_profiles
from octo_api.local_client_api.login import login_octo
from octo_api.local_client_api.logout import logout_octo
# from octo_api.local_client_api.open_profile import open_profile_by_id
from octo_api.local_client_api.stop_profile import stop_profile
from octo_api.tags.get_tags import get_tags
from octo_api.tags.update_tag import update_tag
from octo_api.tags.create_tag import create_tag
from octo_api.tags.delete_tag import delete_tag
from octo_api.profiles.update_profile import update_profile
from octo_api.profiles.delete_profiles import delete_profiles

from logo_api.LocalRestAPI.open_profile_by_id import  open_profile_by_id
from logo_api.LocalRestAPI.stop_profile_by_id import stop_profile_by_id
from logo_api.my_driver import return_my_driver



from core.farming.day_1.cookies import cookies
from core.farming.day_1.process import process_day_1
# update_profile('8d700ad49f9449988715a1008f305e93', {"title": 'testAPI'})

# from octo_api.my_driver import return_my_driver

# import psutil

# def get_process_by_name(name):
#     """Возврат существующего процесса используя часть его имени"""
#     for proc in psutil.process_iter(['pid', 'name']):
#         if name.lower() in proc.info['name'].lower():
#             return proc.info
#     return None


# def get_ports_by_pid(pid):
#     process = psutil.Process(pid)
#     connections = process.connections(kind='inet')  # Только сетевые соединения
#     ports = [conn.laddr.port for conn in connections if conn.status == 'LISTEN']
#     return ports

# import subprocess

# def get_processes_using_file(application_path):
#     try:
#         # Выполняем команду lsof для поиска процессов, которые используют этот файл
#         result = subprocess.run(
#             ["lsof", "| grep", application_path],
#             capture_output=True,
#             text=True
#         )
        
#         if result.stdout:
#             return result.stdout.splitlines()
#         else:
#             return f"Не найдено процессов, связанных с {application_path}"
#     except Exception as e:
#         return f"Ошибка: {e}"

# # Пример вызова функции:
# application_path = "/Applications/Octo Browser.app/Contents/MacOS/Octo Browser"
# processes = get_processes_using_file(application_path)
# for process in processes:
#     print(process)
    
#     import subprocess

# def get_open_ports_by_process(process_name):
#     command = f"sudo lsof -i -n -P | grep {process_name}"
#     try:
#         process_info = subprocess.check_output(command, shell=True).decode('utf-8')
#         return process_info
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка: {e}")
#         return None

# # Пример использования
# process_name = "Octium"
# open_ports = get_open_ports_by_process(process_name)
# if open_ports:
#     print(open_ports)
    
    
# import subprocess

# def get_process_start_time(pid):
#     # Используем команду ps для получения времени запуска процесса
#     command = f"ps -p {pid} -o lstart="
    
#     try:
#         process_start_time = subprocess.check_output(command, shell=True).decode('utf-8').strip()
#         return process_start_time
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка при получении информации о процессе: {e}")
#         return None

# # Пример использования:
# pid = 58379  # замените на нужный вам PID
# start_time = get_process_start_time(pid)
# if start_time:
#     print(f"Процесс {pid} был запущен: {start_time}")
    
    
try:
    # print('get_process_path_by_port', get_process_path_by_port(58888))
    # print('get_process_by_name', get_process_by_name('Octium'))
    # get_ports_by_pid(get_process_by_name('Octium')['pid'])
    
    driver = return_my_driver(20753, '/Users/mac/Desktop/desktop/scanner/chromedriver/chromedriver-127')
    # driver = driver = open_profile_by_id('66fb0b1bea246fda11920305', '/Users/mac/Desktop/desktop/scanner/chromedriver/chromedriver-127')['driver']
    driver.implicitly_wait(10)
    process_day_1(driver)
    
    
    # print('driver', driver)

    # 
    # process_day_1(driver)
    
except Exception as e:
    print('dlobal level:', e)
    stop_profile_by_id('67100fa3ad086e7ee7870fe1')
    

# driver = stop_profile('5695a319c3aa4ea39642fd92b76e81b3')
# res = delete_profiles(['c570aec53d8d48ec8dfc41b35700c04d', 'e0ab073319d24e43b2136b2b7d492892'])
# driver.get('https://www.youtube.com/')
# print('res', res)