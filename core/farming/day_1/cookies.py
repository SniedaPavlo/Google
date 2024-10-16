from utils.driver import close_all_windows_driver

from utils.driver import search_and_click_to_site
def cookies(driver):
    '''Нагуливаем куки на гигантах'''
    close_all_windows_driver(driver)
    
    search_and_click_to_site(driver, 'amazon+buy+books', 'www.amazon.com')
    