import requests
from data.config import PORT_OCTO

def stop_profile(uuid):
    url = f'http://localhost:{PORT_OCTO}/api/profiles/stop'
    data = {
        "uuid": uuid
    }
    
    try:
        return requests.post(url=url, json=data).json()
    except Exception as e:
        print('Error in function "stop_profile":', e)