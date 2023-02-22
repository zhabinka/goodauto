# Generated by Django 4.1.7 on 2023-02-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0006_car_accessories_car_additional_options_car_body_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="price",
            field=models.DecimalField(
                db_index=True, decimal_places=0, max_digits=7, null=True
            ),
        ),
    ]