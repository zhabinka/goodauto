from storage.models import UrlStorage


def to_storage(url):
    item, created = UrlStorage.objects.get_or_create(external_url=url)
    return item if created else None


def check(url):
    stop_words = ['clc.php']
    for word in stop_words:
        if word in url:
            return False
    return True
