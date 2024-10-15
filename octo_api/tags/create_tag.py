from data.config import OCTO_TOKEN
import requests

def create_tag(name, color=None):
    url = 'https://app.octobrowser.net/api/v2/automation/tags'
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN
    }
    data = {
        'name': name
    }
    if color:
        data["color"] = color
    
    try:
        return requests.post(url=url, headers=headers, json=data).json()
    except Exception as e:
        print('Error in function "create_tag":', e)