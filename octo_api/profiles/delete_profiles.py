import requests

from data.config import OCTO_TOKEN

def delete_profiles(uuids):
    url = 'https://app.octobrowser.net/api/v2/automation/profiles'
    
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN
    }
    
    data = {
        'uuids': uuids,
        'skip_trash_bin': True
    }
    
    try:
        return requests.delete(url=url, headers=headers, json=data).json()
    except Exception as e:
        print('Error in function "delete_profiles":', e)
    