from collections.abc import KeysView
from ctypes import sizeof
from django.db import models
from storage.models import CarModel, HtmlStorage, UrlStorage


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
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(db_index=True, null=True, max_digits=7, decimal_places=0)
    external_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    processed = models.BooleanField(default=False)

    drivable = models.TextField(null=True, blank=True)
    model_year = models.PositiveSmallIntegerField()
    first_registration = models.CharField(max_length=20)
    mileage = models.DecimalField(max_digits=7, decimal_places=0)

    # choice
    fuel_type = models.CharField(max_length=20)
    transmission_type = models.CharField(max_length=50)
    four_wheel_drive = models.CharField(max_length=20)
    co2_emission_standard = models.CharField(max_length=10)

    co2_emission = models.CharField(max_length=20)
    power = models.CharField(max_length=20)
    engine_size = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    doors =  models.PositiveSmallIntegerField()
    number_of_seats = models.PositiveSmallIntegerField()
    number_of_keys = models.PositiveSmallIntegerField()
    paint = models.CharField(max_length=20)
    interior_colour = models.CharField(max_length=20)

    # choice
    vat = models.CharField(max_length=20)
    registration_documents = models.CharField(max_length=20)
    coc = models.CharField(max_length=20)

    # choice
    pickup_location = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=30)
    selling_office = models.CharField(max_length=30)

    high_value_equipment = models.TextField(null=True, blank=True)
    additional_options = models.TextField(null=True, blank=True)
    accessories = models.TextField(null=True, blank=True)

    damage = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'cars'
