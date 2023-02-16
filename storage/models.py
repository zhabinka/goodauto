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
