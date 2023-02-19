from django.db import models


class UrlStorage(models.Model):

    class Type(models.IntegerChoices):
        SINGLE = 1, 'single'
        BUNCH = 2, 'bunch'

    external_url = models.URLField(max_length=255, unique=True)
    processed = models.BooleanField(default=False)
    type_url = models.PositiveSmallIntegerField(choices=Type.choices, default=Type.SINGLE)

    class Meta:
        db_table = 'url_storage'


class HtmlStorage(models.Model):
    url_storage = models.ForeignKey(
        UrlStorage,
        on_delete=models.CASCADE,
    )
    source_html = models.TextField()
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'html_storage'


class Brand(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    class Meta():
        db_table = 'brands'
        unique_together = ['manufacturer', 'model']


class UrlBunchStorage(models.Model):
    node_url = models.URLField(max_length=255)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
    )

    class Meta():
        db_table = 'url_bunche_storage'
