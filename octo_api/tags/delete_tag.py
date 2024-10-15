

from data.config import OCTO_TOKEN
import requests

def delete_tag(uuid):
    url = f'https://app.octobrowser.net/api/v2/automation/tags/{uuid}'
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN
    }
    try:
        return requests.delete(url=url, headers=headers).json()
    except Exception as e:
        print('Error in function "delete_tag":', e)