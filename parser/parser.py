import time
import os
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')
CHROME_DRIVER_PATH = os.path.join(BASE_PATH, 'chromedriver')
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)

SOURCE_URL = 'https://www.blocket.se'
CATALOG_PATH = '/annonser/hela_sverige/fordon/bilar?cg=1020'


def init_chrome_webdriver():
    # TODO: add header (user-agent etc.)
    return webdriver.Chrome(service=CHROME_SERVICE)


def collect_catalog_page_sources(url, pages_count=3):
    driver = init_chrome_webdriver()
    source_dir = os.path.join(ASSETS_PATH, 'pages')

    os.makedirs(source_dir, exist_ok=True)

    try:
        counter = 1
        while counter <= pages_count:
            current_page_url = f'{url}&page={counter}'
            current_page_source_path = f'{source_dir}/{counter}.html'

            driver.get(url=current_page_url)
            time.sleep(2)

            with open(current_page_source_path, 'w') as f:
                f.write(driver.page_source)

            # TODO: add logging
            print(f'[INFO] Downloaded page {counter} to {current_page_source_path}')
            counter += 1

    except Exception as e:
        # TODO: add logging
        # TODO: retry requests
        print(e)
    finally:
        driver.close()
        driver.quit()
