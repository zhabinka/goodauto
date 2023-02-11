import os
import json
import time
from bs4 import BeautifulSoup

from django.db import transaction

from sheduler.driver import init_chrome_webdriver
from sheduler.models import CrawlFrontier
from storage.models import HtmlStorage, UrlStorage
from sheduler.parser import add_parser_task
from storage import url

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ASSETS_CAR_LINKS_PATH = os.path.join(BASE_PATH, 'links.json')


def add_crawl_task(url_):
    item = url.to_storage(url_)
    if item:
        id = CrawlFrontier.objects.create(url_storage=item)
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
    tasks = CrawlFrontier.objects.all()

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

