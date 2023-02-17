from django.core.management import BaseCommand

from storage.models import UrlType


class Command(BaseCommand):

    def handle(self, *args, **options):
        if UrlType.objects.exists():
            print('[INFO] Data already loaded...exiting.')
            return

        print("[INFO] Loading data")

        url_types = [
            (1, 'single'),
            (2, 'bunch'),
        ]

        for _, type_name in url_types:
            type = UrlType(name=type_name)
            type.save()

        print("[SUCCESS] All types loaded")
