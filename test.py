from octo_api.profiles.get_profiles import get_profiles
from octo_api.profiles.create_profile import create_profiles
from octo_api.local_client_api.login import login_octo
from octo_api.local_client_api.logout import logout_octo
from octo_api.local_client_api.open_profile import open_profile_by_id
from octo_api.local_client_api.stop_profile import stop_profile
from octo_api.tags.get_tags import get_tags
from octo_api.tags.update_tag import update_tag
from octo_api.tags.create_tag import create_tag
from octo_api.tags.delete_tag import delete_tag
from octo_api.profiles.update_profile import update_profile
from octo_api.profiles.delete_profiles import delete_profiles

from core.farming.day_1.cookies_2 import cookies
from core.farming.day_1.process import process_day_1
# update_profile('8d700ad49f9449988715a1008f305e93', {"title": 'testAPI'})

try:
    driver = open_profile_by_id('8d700ad49f9449988715a1008f305e93')
    driver.implicitly_wait(10)
    process_day_1(driver)
except Exception as e:
    stop_profile('8d700ad49f9449988715a1008f305e93')
    print('dlobal level:', e)

# driver = stop_profile('5695a319c3aa4ea39642fd92b76e81b3')
# res = delete_profiles(['c570aec53d8d48ec8dfc41b35700c04d', 'e0ab073319d24e43b2136b2b7d492892'])
# driver.get('https://www.youtube.com/')
# print('res', res)