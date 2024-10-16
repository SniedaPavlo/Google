from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from urllib.parse import urlparse

def connect(response_json, path_achromedriver, additional_options):
    print('response_json connect anty:', response_json)
    # Получение URL WebSocket из ответа
    ws_url = response_json["wsUrl"]

    # Извлечение порта из URL WebSocket
    parsed_url = urlparse(ws_url)
    port = str(parsed_url.port) 
    
    # Initializing the webdriver and adding options
    chrome_path = Service(path_achromedriver)
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

    return {"driver": driver, "port": port}

# example
#--------------------------------------------------------------------
# response_json = {"automation": {"port": 9222}}
# additional_options = {"headless": True, "start-maximized": True}

# driver = connect(response_json, additional_options)