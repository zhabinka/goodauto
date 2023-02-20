from django.db import models


class CarModel(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    class Meta():
        db_table = 'car_models'
        unique_together = ['brand', 'model']


class UrlStorage(models.Model):
    external_url = models.URLField(max_length=255, unique=True)
    processed = models.BooleanField(default=False)
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'url_storage'


class HtmlStorage(models.Model):
    url_storage = models.OneToOneField(
        UrlStorage,
        on_delete=models.CASCADE,
    )
    source_html = models.TextField()
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'html_storage'


class UrlBunchStorage(models.Model):
    node_url = models.URLField(max_length=255)
    car_model = models.OneToOneField(
        CarModel,
        on_delete=models.CASCADE,
    )
    processed = models.BooleanField(default=False)

    class Meta():
        db_table = 'url_bunch_storage'


class HtmlBunchStorage(models.Model):
    url_bunch_storage = models.OneToOneField(
        UrlBunchStorage,
        on_delete=models.CASCADE,
    )
    source_html = models.TextField()
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'html_bunch_storage'
