import os
import json
import time
import random

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

from django.db import transaction

from sheduler.driver import init_chrome_webdriver
from sheduler.models import CrawlerFrontier
from storage.models import HtmlStorage, UrlBunchStorage, UrlStorage, HtmlBunchStorage
from sheduler.parser import add_parser_task
from storage import url

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ASSETS_CAR_LINKS_PATH = os.path.join(BASE_PATH, 'links.json')

def add_crawl_task(url_):
    item = url.to_storage(url_)
    if item:
        id = CrawlerFrontier.objects.create(url_storage=item)
        print(f'Add {item.external_url} in sheduler')
        return id


def collect():
    with open(ASSETS_CAR_LINKS_PATH, 'r') as f:
        cars = json.load(f)

    for car in cars[:10]:
        url_ = car['url']
        if url.check(url_):
            add_crawl_task(url_)


def scrapy():
    driver = init_chrome_webdriver()
    tasks = CrawlerFrontier.objects.all()

    try:
        for task in tasks[:10]:
            url = task.url_storage.external_url
            driver.get(url=url)
            time.sleep(10)

            item, _ = HtmlStorage.objects.get_or_create(
                url_storage=task.url_storage
            )

            page = BeautifulSoup(driver.page_source, 'lxml')
            useful_html = page.select('article[class*=AdMotor__Article]')

            item.source_html = useful_html
            item.save()

            add_parser_task(item)

            print(f'[INFO] Downloaded html from {url}')

            url_storage = UrlStorage.objects.get(external_url=url)
            url_storage.processed = True

            with transaction.atomic():
                task.delete()
                url_storage.save()
                print(f'[INFO] Removed {url} from sheduler')

    except Exception as e:
        print(f'[ERROR] {e}')
    finally:
        driver.close()
        driver.quit()

    print(f'[INFO] All tasks complited')


def scrapy_bunches():
    for bunch in UrlBunchStorage.objects.filter(processed=False):
        scrapy_bunch(bunch)
        print(f'[SUCCESS] {bunch.node_url}')


def scrapy_bunch(bunch):
    driver = init_chrome_webdriver()
    html = []

    try:
        driver.get(url=bunch.node_url)

        while True:
            time.sleep(random.randint(8, 10))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            soup = BeautifulSoup(driver.page_source, 'lxml')
            useful_html = soup.find('div', class_='rc-CarsResultList')
            html.append(str(useful_html))

            next = driver.find_elements(By.XPATH, "//li[@class='next']/a")

            if len(next):
                time.sleep(random.randint(3, 5))
                next[0].click()
            else:
                html_bunch, _ = HtmlBunchStorage.objects.get_or_create(
                    url_bunch_storage=bunch
                )
                html_bunch.source_html = ''.join(html)
                bunch.processed = True

                with transaction.atomic():
                    bunch.save()
                    html_bunch.save()

                return

    except Exception as e:
        # TODO: add logging
        # TODO: retry requests
        print(f'[ERROR] {e}')
    finally:
        driver.close()
        driver.quit()
        print(f'[SUCCESS] All bunches downloaded')
