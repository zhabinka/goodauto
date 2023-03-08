import os
from csv import DictReader
from django.core.management import BaseCommand

from storage.models import CarModel, UrlBunchStorage


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ASSETS_CAR_MODELS_PATH = os.path.join(BASE_PATH, '../../fixtures/cars.csv')

# https://adityakedawat.medium.com/importing-csv-file-into-django-models-using-django-management-command-716eda305e61
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(ASSETS_CAR_MODELS_PATH, newline='') as csvfile:
            reader = DictReader(csvfile,  delimiter=';')
            for row in reader:
                model = f'{row["mark"]} {row["model"]}'
                car_model, created = CarModel.objects.get_or_create(
                    brand=row['mark'],
                    model=row['model'],
                )
                if created:
                    car_model.save()
                    print(f'[INFO] Loaded model {model}')

                adesa_url = row['adesa']
                if adesa_url:
                    bunch, _ = UrlBunchStorage.objects.get_or_create(
                        car_model=car_model,
                    )
                    bunch.node_url=adesa_url
                    bunch.save()
                    print(f'[INFO] Add url {adesa_url} to {model}')

        print('[SUCCESS] All brands loaded')
