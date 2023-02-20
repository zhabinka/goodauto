import re
import urllib

from bs4 import BeautifulSoup
from url_normalize import url_normalize

from django.db import transaction

from sheduler.models import ParserFrontier
from storage.models import HtmlBunchStorage, HtmlStorage, UrlStorage
from goodauto.cars.views import to_storage


def add_parser_task(html_storage_item):
    car = to_storage(html_storage_item)

    id = ParserFrontier.objects.create(
        car=car,
        html_storage=html_storage_item,
    )
    print(f'Add car.id={car.id} in sheduler (id={id})')
    return id


def parse():
    # car.find('a')['href']
    # car.find('h3').find('span').text

    tasks = ParserFrontier.objects.all()
    for task in tasks[:2]:
        html = task.html_storage.source_html
        page = BeautifulSoup(html, 'lxml')
        price_source = page.select('div[class*=PriceWrapper]')
        if price_source:
            price = page.select('div[class*=PriceWrapper]')[0].find('div')
            title = page.find('h1')
            item = task.car
            item.price = int(re.sub('[^0-9]', '', price.text))
            item.name = title.text
            item.url_storage = task.html_storage.url_storage
            print(item)
            print(price)
            print(title)
            print(task.html_storage.url_storage)
            item.save()

        # html_storage = HtmlStorage.objects.get(source_html=html)
        html_storage = task.html_storage
        html_storage.processed = True

        with transaction.atomic():
            task.delete()
            html_storage.save()
            print(f'[SUCCESS] Added car')
            print(f'[] Removed task')

    print(f'[INFO] All task complited')


def normalize(path):
    url = urllib.parse.urljoin('//www.adesa.eu', path)
    return url_normalize(url)
