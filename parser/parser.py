import time
import os
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')
ASSETS_CATALOG_PAGES_PATH = os.path.join(ASSETS_PATH, 'pages')
CHROME_DRIVER_PATH = os.path.join(BASE_PATH, 'chromedriver')
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)

SOURCE_URL = 'https://www.blocket.se'
CATALOG_PATH = '/annonser/hela_sverige/fordon/bilar?cg=1020'


def init_chrome_webdriver():
    # TODO: add header (user-agent etc.)
    return webdriver.Chrome(service=CHROME_SERVICE)


def collect_catalog_page_sources(url, pages_count=3):
    driver = init_chrome_webdriver()
    os.makedirs(ASSETS_CATALOG_PAGES_PATH, exist_ok=True)

    try:
        counter = 1
        while counter <= pages_count:
            current_page_url = f'{url}&page={counter}'
            current_page_source_path = f'{ASSETS_CATALOG_PAGES_PATH}/{counter}.html'

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


def get_links_auto(dir_path):
    files = os.listdir(dir_path)
    autos = []
    target_url = 'clc.php'

    for file in files:
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r') as f:
            source = f.read()
            page = BeautifulSoup(source, 'lxml')
            items = page.find_all('div', class_='styled__Wrapper-sc-1kpvi4z-0')

            for item in items:
                link = item.find('a', class_='styled__StyledTitleLink-sc-1kpvi4z-11').get('href')
                # expclude target links
                if target_url in link:
                    continue

                *_, id = link.split('/')
                autos.append({
                                 'id': int(id),
                                 'url': f'{SOURCE_URL}{link}',
                             })

        print(f'[SUCCESS] Page {filepath} processed')

    # TODO: записать в базу
    with open(os.path.join(ASSETS_PATH, 'links.json'), 'w') as f:
        json.dump(autos, f, indent=4, ensure_ascii=False)
