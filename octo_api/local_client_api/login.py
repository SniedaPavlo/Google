from data.config import PORT_OCTO, LOGIN

import requests

def login_octo():
    url = f'http://localhost:{PORT_OCTO}/api/auth/login'
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        "email": LOGIN['USERNAME'],
        "password": LOGIN["PASSWORD"]
    }
    
    try:
        res = requests.post(url=url, headers=headers, json=data)
        return res.json()
    except Exception as e:
        print('Error in function "login_octo":', e)
        
        
        
        
        
        