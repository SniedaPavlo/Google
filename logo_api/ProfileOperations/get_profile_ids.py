import requests
from src.data.config import TOKEN

def get_profile_ids(limit=1000, page=1):
    url = 'https://api.gologin.com/browser/v2'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    params = {
        'limit': limit,
        'page': page,
        'sorterField': 'createdAt',
        'sorterOrder': 'descend'
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        profiles_data = response.json().get('profiles', [])
        profile_ids = [profile['id'] for profile in profiles_data]
        return profile_ids
    else:
        print(f"Failed to fetch profiles. Status code: {response.status_code}")
        return []

# # Пример использования:
# api_token = 'YOUR_API_TOKEN'
# profile_ids = get_profile_ids(api_token)
# print(profile_ids)
