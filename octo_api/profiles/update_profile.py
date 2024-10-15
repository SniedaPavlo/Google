import requests

from data.config import OCTO_TOKEN

def update_profile(uuid, data):
    url = f'https://app.octobrowser.net/api/v2/automation/profiles/{uuid}'
    headers = {
        'X-Octo-Api-Token': OCTO_TOKEN
    }
    
    try:
        return requests.patch(url=url, headers=headers, json=data).json() 
    except Exception as e:
        print('Error in function "update_profile" :', e)
        
    
    
# example data:
# {
#     "title": "new title", // [optional]
#     "description": "new description", // [optional]
#     "start_pages": ["https://fb.com"],
#         "bookmarks": [{
#         "name": "example42",
#         "url": "http://example.com"
#     }],
#     "tags": [ // [optional]
#         "new_tag"
#     ],
#     "pinned_tag": "octo", // [optional],
#     "proxy": { // [optional]
#         "type": "socks5",
#         "host": "1.1.1.1",
#         "port": 5555,
#         "login": "",
#         "password": ""
#     },
#     "storage_options": { // [optional]
#         "cookies": true,
#         "passwords": true,
#         "extensions": true,
#         "localstorage": false,
#         "history": false,
#         "bookmarks": true
#     },
#     "cookies": [ // [optional]
#     {
#       "domain": ".google.com",
#       "expirationDate": 1639134293.313654,
#       "hostOnly": false,
#       "httpOnly": false,
#       "name": "1P_JAR",
#       "path": "/",
#       "sameSite": "no_restriction",
#       "secure": true,
#       "value": "2021-11-10-11"
#     }
#     ],
#     "image": "36fb48f4e99d47d3b18383d0c27feac2", // [optional]
#     "extensions": [], // [optional]
#     "fingerprint": { // [optional]
#         "os": "win", // [required]
#         "os_version": "11", // [optional]
#         "os_arch": "x86", // [optional]
#         "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
#         "screen": "1920x1080",
#         "languages": {
#             "type": "ip"
#         },
#         "timezone": {
#             "type": "ip"
#         },
#         "geolocation": {
#             "type": "ip"
#         },
#         "cpu": 4,
#         "ram": 8,
#         "noise": {
#             "webgl": true,
#             "canvas": false,
#             "audio": true,
#             "client_rects": false
#         },
#         "webrtc": {
#             "type": "ip"
#         },
#         "dns": "1.1.1.1",
#         "media_devices": {
#             "video_in": 1,
#             "audio_in": 1,
#             "audio_out": 1
#         }
#     }
# }