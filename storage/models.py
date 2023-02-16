from django.db import models


class UrlStorage(models.Model):
    external_url = models.URLField(max_length=255, unique=True)
    processed = models.BooleanField(default=False)


class HtmlStorage(models.Model):
    url_storage = models.ForeignKey(
        UrlStorage,
        on_delete=models.CASCADE,
    )
    source_html = models.TextField()
    processed = models.BooleanField(default=False)


class Provider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255, unique=True)

    class Meta:
        db_table = 'providers'


class Brand(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    class Meta():
        db_table = 'brands'
        unique_together = ['manufacturer', 'model']


class UrlBunch(models.Model):
    node_url = models.URLField(max_length=255)
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
    )

    class Meta():
        db_table = 'url_bunches'
