from django.db import models
from goodauto.cars.models import Car
from storage.models import HtmlStorage, UrlStorage


class CrawlerFrontier(models.Model):
    url_storage = models.ForeignKey(
        UrlStorage,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'crawl_frontier'

class ParserFrontier(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    html_storage = models.ForeignKey(
        HtmlStorage,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'parser_frontier'
