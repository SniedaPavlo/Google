from data.config import OCTO_TOKEN
import requests

def update_tag(tag_uuid, tag, color=None):
    url = f"https://app.octobrowser.net/api/v2/automation/tags/{tag_uuid}"
    headers = {
        "Content-Type": "application/json",
        "X-Octo-Api-Token": OCTO_TOKEN
    }
    data = {
        "name": tag
    }
    if color:
        data["color"] = color
        
    try:
        return requests.patch(url=url, headers=headers, json=data).json()
    except Exception as e:
        print('Error in function "update_tag":', e)
    
    