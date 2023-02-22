import os
import json
import time
import random
import re

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

from django.db import transaction

from sheduler.driver import init_chrome_webdriver
from sheduler.models import CrawlerFrontier
from storage.models import HtmlStorage, UrlBunchStorage, UrlStorage, HtmlBunchStorage


def add_crawler_tasks():
    car_urls = UrlStorage.objects.filter(processed=False)

    for car_url in car_urls:
        url = car_url.external_url
        task, created = CrawlerFrontier.objects.get_or_create(
            url_storage=car_url,
        )
        print(f'[{created}] {url} in sheduler {task}')


def scrapy(limit=2):
    driver = init_chrome_webdriver()
    tasks = CrawlerFrontier.objects.all()[:limit]

    try:
        for task in tasks:
            url = task.url_storage.external_url
            driver.get(url=url)
            time.sleep(random.randint(8, 12))

            html_storage, _ = HtmlStorage.objects.get_or_create(
                url_storage=task.url_storage
            )

            soup = BeautifulSoup(driver.page_source, 'lxml')
            useful_html = soup.find('div', class_=re.compile('cardetail-container'))

            html_storage.source_html = str(useful_html)
            html_storage.processed = False
            html_storage.save()

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
        print(f'[SUCCESS] All bunches for {bunch.car_model.brand} {bunch.car_model.model} downloaded')
