from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from data.config import PATH_TO_CHROMEDRIVER

def connect(port, additional_options=None):
    # Initializing the webdriver and adding options
    chrome_path = Service(PATH_TO_CHROMEDRIVER)
    options = webdriver.ChromeOptions()

    # Checking for additional options and adding them if they exist
    if additional_options:
        for key, value in additional_options.items():
            options.add_argument(f"--{key}={value}")

    # Connecting the webdriver to an existing instance (specifying the path to our instance as I understand it)
    # debugger_address = "debugger" refers to the Chrome debugging port.
    options.debugger_address = "127.0.0.1:" + port
    # Initialization must be after options.debugger_address to trigger linking and connect the debugger to the desired port and address
    driver = webdriver.Chrome(service=chrome_path, options=options)

    return {"driver": driver, "port": str(port)}

# example
#--------------------------------------------------------------------
# response_json = {"automation": {"port": 9222}}
# additional_options = {"headless": True, "start-maximized": True}

# driver = connect(response_json, additional_options)