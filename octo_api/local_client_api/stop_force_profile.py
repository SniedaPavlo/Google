import requests
from data.config import PORT_OCTO

def stop_force_profile(uuid):
    url = f'http://localhost:{PORT_OCTO}/api/profiles/force_stop'
    data = {
        "uuid": uuid
    }
    
    try:
        return requests.post(url=url, json=data).json()
    except Exception as e:
        print('Error in function "stop_force_profile":', e)