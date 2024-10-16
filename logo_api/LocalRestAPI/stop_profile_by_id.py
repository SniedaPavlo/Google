
import requests

def stop_profile_by_id(id):
    req_url = 'http://localhost:36912/browser/stop-profile'
    data = {
        "profileId": id,
    }

    # Отправка запроса и получение ответа от сервера
    response = requests.post(req_url, json=data)
    print("response stop profile", response)

    return response
