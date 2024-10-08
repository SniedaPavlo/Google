import requests

from data.config import OCTO_TOKEN

def get_profiles(**kwargs):

    url = 'https://app.octobrowser.net/api/v2/automation/profiles'
    
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN
    }
    
    params = {
        'page_len': 100,
        'page': 0,
        'fields': 'title,description,proxy,start_pages,tags,status,last_active,version,storage_options,created_at,updated_at',
        'ordering': 'active'
    }
    params.update(kwargs)
    
    try:
        res = requests.get(url=url, headers=headers, params=params)
        return res.json() 
    except Exception as e:
        print('Error in function "get_profiles" :', e)
        
#exapmle 
# result = get_profiles(api_token='your_token', search='profile_title', search_tags='tag1,tag2', status=1, password=True)

