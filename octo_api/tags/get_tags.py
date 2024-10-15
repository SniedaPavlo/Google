from data.config import OCTO_TOKEN

import requests

def get_tags():
    
    url = 'https://app.octobrowser.net/api/v2/automation/tags'
    
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN
    }
    
    try:
        return requests.get(url=url, headers=headers).json()
    except Exception as e:
        print('Error in function "get_tags":', e)