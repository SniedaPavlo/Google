
import requests
from logo_api.connect import connect

def open_profile_by_id(id, path_achromedriver, additional_options=None):
    # Создание URL на основе соединения. Передача динамического идентификатора
    req_url = 'http://localhost:36912/browser/start-profile'
    data = {
        "profileId": id,
        "sync": True
    }

    # Отправка запроса и получение ответа от сервера
    response = requests.post(req_url, json=data)
    
    # Преобразование ответа в формат JSON
    response_json = response.json()
    print('response_json', response.json())
    
    # Передача информации о запросе для вызова драйвера
    dictionary_driver = connect(response_json, path_achromedriver,  additional_options=additional_options)

    return dictionary_driver