from collections.abc import KeysView
from ctypes import sizeof
from django.db import models
from storage.models import CarModel, HtmlStorage, UrlStorage


class Car(models.Model):
    url_storage = models.OneToOneField(
        UrlStorage,
        on_delete=models.CASCADE,
        related_name='car',
    )
    html_storage = models.OneToOneField(
        HtmlStorage,
        on_delete=models.RESTRICT,
        related_name='car',
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
    closed = models.BooleanField(default=False)

    # no
    drivable = models.TextField(null=True, blank=True)

    model_year = models.PositiveSmallIntegerField(null=True, blank=True,)
    first_registration = models.CharField(null=True, blank=True, max_length=100)
    mileage = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=0)

    # choice
    fuel_type = models.CharField(null=True, blank=True, max_length=100)
    transmission_type = models.CharField(null=True, blank=True, max_length=100)
    four_wheel_drive = models.CharField(null=True, blank=True, max_length=100)
    co2_emission_standard = models.CharField(null=True, blank=True, max_length=10)

    co2_emission = models.CharField(null=True, blank=True, max_length=100)
    power = models.CharField(null=True, blank=True, max_length=100)
    engine_size = models.CharField(null=True, blank=True, max_length=100)
    body_type = models.CharField(null=True, blank=True, max_length=100)
    doors_count =  models.PositiveSmallIntegerField(null=True, blank=True)
    seats_count = models.PositiveSmallIntegerField(null=True, blank=True)
    keys_count = models.PositiveSmallIntegerField(null=True, blank=True)
    paint = models.CharField(null=True, blank=True, max_length=100)
    interior_colour = models.CharField(null=True, blank=True, max_length=100)

    # choice
    vat = models.CharField(null=True, blank=True, max_length=100)
    registration_documents = models.CharField(null=True, blank=True, max_length=100)
    coc = models.CharField(null=True, blank=True, max_length=100)

    # choice
    pickup_location = models.CharField(null=True, blank=True, max_length=255)
    origin_country = models.CharField(null=True, blank=True, max_length=30)
    selling_office = models.CharField(null=True, blank=True, max_length=30)

    equipment = models.TextField(null=True, blank=True)
    high_value_equipment = models.TextField(null=True, blank=True)
    additional_options = models.TextField(null=True, blank=True)
    accessories = models.TextField(null=True, blank=True)

    damage = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return f'{self.name}'

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Car._meta.fields]
