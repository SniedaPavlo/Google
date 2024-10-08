import requests

from data.config import OCTO_TOKEN

def create_profiles():
    url = 'https://app.octobrowser.net/api/v2/automation/profiles'
    
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN,
        'Content-Type': 'application/json'
    }
    
    data = {
        "title": "Test profile from api",
        "fingerprint": {
            "os": "win",
        }
    }
    
    try:
        res = requests.post(url=url, headers=headers, json=data)
        return res.json()
    except Exception as e:
        print('Error in function "create_profile":', e)