import os

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CHROME_DRIVER_PATH = os.path.join(BASE_PATH, 'chromedriver')
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)

def init_chrome_webdriver():
    # TODO: options.add_argument('--proxy-server=198.199.120.102:8080')
    user_agent = UserAgent(browsers=['chrome']).random

    # chromedriver options description
    # https://peter.sh/experiments/chromium-command-line-switches/
    options = Options()

    # test user-agent https://whatmyuseragent.com/
    options.add_argument(f'user-agent={user_agent}')

    # disable webdriver mode
    # https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html
    options.add_argument('--disable-blink-features=AutomationControlled')

    # use background mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(service=CHROME_SERVICE, options=options)
