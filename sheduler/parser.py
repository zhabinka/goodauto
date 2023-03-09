import re
import urllib

from bs4 import BeautifulSoup
from url_normalize import url_normalize

from django.db import transaction

from sheduler.models import ParserFrontier
from storage.models import HtmlBunchStorage, HtmlStorage, UrlStorage
from goodauto.cars.models import Car
from goodauto.cars.views import to_storage
from storage.url import check


def add_parser_tasks():
    html_storages = HtmlStorage.objects.filter(processed=False)

    for html_storage in html_storages:
        car = to_storage(html_storage)
        task, created = ParserFrontier.objects.get_or_create(
            car=car,
            html_storage=html_storage,
        )
        print(f'[Task created: {created}] {car} in sheduler {task}')


def pull_numbers(bs):
    text = bs.text if bs else '0'
    return int(re.sub('[^0-9]', '', text))


def parse(limit=None):
    tasks = ParserFrontier.objects.all()[:limit]

    for task in tasks:
        car = Car.objects.get(id=task.car.id)
        html_storage = HtmlStorage.objects.get(id=task.html_storage.id)
        soup = BeautifulSoup(html_storage.source_html, 'lxml')
        # TODO: Учитывать статус аукциона (закрыт, продан)
        if not soup.find('div', class_='rc-AuctionClosedPanel') and not soup.find('div', class_='rc-SoldCarPanel'):
            h1 = soup.find('h1')
            name, *_ = h1.text.split(' - ')
            car.name = name
            price_block = soup.find('div', class_='rc-BiddingAdvisorPanel')
            if price_block :
                car.price =  pull_numbers(price_block.find('div', class_='col'))
            # external_id = soup.select('div[class*=uitest-refnr]')
            # car.external_id = pull_numbers(external_id.text)
            model_year_raw = soup.find('div', {'data-attr': 'car-model-year'})
            car.model_year = pull_numbers(model_year_raw)
            car.first_registration = soup.find('div', {'data-attr': 'car-first-registration'}).text
            mileage_raw = soup.find('div', {'data-attr': 'car-mileage'})
            car.mileage = pull_numbers(mileage_raw)
            car.fuel_type = soup.find('div', {'data-attr': 'car-fuel'}).text
            car.transmission_type = soup.find('div', {'data-attr': 'car-transmission'}).text

            # Не у всех авто
            # four_wheel_drive = soup.find('div', {'data-attr': 'car-fuel'}).text
            # co2_emission_standard, co2_emission = soup.find_all('div', {'data-attr': 'car-emission'})
            # car.co2_emission_standard = co2_emission_standard.text
            # car.co2_emission = co2_emission.text

            car.power = soup.find('div', {'data-attr': 'car-kw'}).text
            car.engine_size = soup.find('div', {'data-attr': 'car-engine'}).text
            car.body_type = soup.find('div', {'data-attr': 'car-body'}).text
            doors_count_raw = soup.find('div', {'data-attr': 'car-doors'})
            car.doors = pull_numbers(doors_count_raw)
            seats_count_raw = soup.find('div', {'data-attr': 'car-places'})
            car.seats_count = pull_numbers(seats_count_raw)

            # car.keys_count = soup.find('div', {'data-attr': 'car-fuel'}).text
            car.paint = soup.find('div', {'data-attr': 'car-paint'}).text
            interior_colour_raw = soup.find('div', {'data-attr': 'car-interior'})
            if interior_colour_raw:
                car.interior_colour = interior_colour_raw.text

            # car.vat = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.registration_documents = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.coc = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.pickup_location = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.origin_country = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.selling_office = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.high_value_equipment = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.additional_options = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.accessories = soup.find('div', {'data-attr': 'car-fuel'}).text
            # car.damage = soup.find('div', {'data-attr': 'car-fuel'}).text
            equipment_raw = soup.find('div', class_='rc-CarEquipment')
            equipment = []

            for item in equipment_raw.find_all('li'):
                content = item.text
                equipment.append(f'<li>{content.strip()}</li>')

            car.equipment = f'<ul>{"".join(equipment)}</ul>'

            car.save()
            print(f'[SUCCESS] Авто {car.name} ({car.id}) обработано {html_storage.url_storage.external_url}')
        else:
            car.closed = True
            car.save()
            print(f'[FAIL] Аукцион закрыт {html_storage.url_storage.external_url} (ID авто {car.id})')

        with transaction.atomic():
            html_storage.processed = True
            html_storage.save()
            id = task.id
            task.delete()
            print(f'[INFO] Задача {id} удалена из очереди')

    print(f'[INFO] Complited {len(tasks)} tasks')
    return


def parse_bunches():
    for bunch in HtmlBunchStorage.objects.all():
        parse_bunch(bunch)
        car_model=bunch.url_bunch_storage.car_model,
        print(f'[Success] All cars {car_model[0]} processed')


def parse_bunch(bunch):
    soup = BeautifulSoup(bunch.source_html, 'lxml')

    for car in soup.find_all('section', class_=re.compile('CarCard')):
        path = car.find('a')['href']
        url = normalize(path)

        # URLs filter
        if not check(url):
            print(f'[INFO] Url {url} does not match')
            continue

        # Было в отдельной функции to_storage (to_sheduler)
        url_storage, created = UrlStorage.objects.get_or_create(
            external_url=url,
        )
        if created:
            url_storage.car_model = bunch.url_bunch_storage.car_model
            url_storage.save()
            print(f'[INFO] Ссылка {url_storage.external_url}({url_storage.id}) добавлена в хранилище')
        # else:
        #     print(f'ссылка {url_storage.id} уже есть в хранилище')

    bunch.processed=True
    bunch.save()


def normalize(path):
    url = urllib.parse.urljoin('//www.adesa.eu', path)
    return url_normalize(url)
