from django.db import models
from storage.models import HtmlStorage, UrlStorage


class Car(models.Model):
    url_storage = models.OneToOneField(
        UrlStorage,
        on_delete=models.PROTECT,
        related_name='url',
    )
    html_storage = models.OneToOneField(
        HtmlStorage,
        on_delete=models.PROTECT,
        related_name='html',
    )
    name = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(db_index=True, null=True)
    external_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cars'
