from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def return_my_driver(port, path_to_chromedriver):
    # Initializing the webdriver and adding options
    chrome_path = Service(path_to_chromedriver)
    options = webdriver.ChromeOptions()

    # Connecting the webdriver to an existing instance (specifying the path to our instance as I understand it)
    # debugger_address = "debugger" refers to the Chrome debugging port.
    options.debugger_address = "127.0.0.1:" + str(port)
    # Initialization must be after options.debugger_address to trigger linking and connect the debugger to the desired port and address
    driver = webdriver.Chrome(service=chrome_path, options=options)
    print('driver', driver)

    return driver
