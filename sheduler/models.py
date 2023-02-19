from django.db import models
from goodauto.cars.models import Car
from storage.models import HtmlStorage, UrlStorage, Type


class CrawlerFrontier(models.Model):
    url_storage = models.ForeignKey(
        UrlStorage,
        on_delete=models.CASCADE,
    )
    type_url = models.PositiveSmallIntegerField(choices=Type.choices, default=Type.SINGLE)
    created_at = models.DateTimeField(auto_now_add=True)


class ParserFrontier(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    html_storage = models.ForeignKey(
        HtmlStorage,
        on_delete=models.CASCADE,
    )
    type_url = models.PositiveSmallIntegerField(choices=Type.choices, default=Type.SINGLE)
    created_at = models.DateTimeField(auto_now_add=True)
