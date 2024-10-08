import requests
from data.config import PORT_OCTO

def logout_octo():
    url = f'http://localhost:{PORT_OCTO}/api/auth/logout'
    
    try:
        res = requests.post(url=url)
        return res.json()
    except Exception as e:
        print('Error in function "logout":', e)