import os
from csv import DictReader
from django.core.management import BaseCommand

from storage.models import Brand


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ASSETS_CAR_MODELS_PATH = os.path.join(BASE_PATH, '../../fixtures/cars.csv')

# https://adityakedawat.medium.com/importing-csv-file-into-django-models-using-django-management-command-716eda305e61
class Command(BaseCommand):

    def handle(self, *args, **options):
        if Brand.objects.exists():
            print('[INFO] Data already loaded...exiting.')
            return

        print("[INFO] Loading data")

        with open(ASSETS_CAR_MODELS_PATH, newline='') as csvfile:
            reader = DictReader(csvfile,  delimiter=';')
            for row in reader:
                car = Brand(
                    manufacturer=row['mark'],
                    model=row['model'],
                )
                car.save()

        print("[SUCCESS] All brands loaded")
