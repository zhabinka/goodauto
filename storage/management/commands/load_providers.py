from django.core.management import BaseCommand

from storage.models import Provider


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Provider.objects.exists():
            print('[INFO] Data already loaded...exiting.')
            return

        print("[INFO] Loading data")

        providers = [
            ('Adesa', 'https://www.adesa.eu/'),
        ]

        for name, url in providers:
            provider = Provider(name=name, url=url)
            provider.save()

        print("[SUCCESS] All providers loaded")
