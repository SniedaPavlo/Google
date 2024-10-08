from octo_api.profiles.get_profiles import get_profiles
from octo_api.profiles.create_profile import create_profiles
from octo_api.local_client_api.login import login_octo
from octo_api.local_client_api.logout import logout_octo
from octo_api.local_client_api.open_profile import open_profile_by_id
from octo_api.local_client_api.stop_profile import stop_profile
driver = stop_profile('5695a319c3aa4ea39642fd92b76e81b3')
# driver.get('https://www.youtube.com/')
print('res', driver)

