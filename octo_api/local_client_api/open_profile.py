import requests
from data.config import PORT_OCTO

from octo_api.local_client_api.connect import connect

def open_profile_by_id(uuid, flags=None, password=None):
    url = f'http://localhost:{PORT_OCTO}/api/profiles/start'
    
    if flags is None:
        flags = []
    
    data = {
        "uuid": uuid,
        "headless": False, 
        "debug_port": True, 
        "timeout": 120,
        "only_local": True,
        "flags": [],
    }

    if password:
        data["password"] = password

    res = requests.post(url=url, json=data)
    port = res.json()['debug_port']
    driver = connect(port)['driver']
    return driver
