# Generated by Django 4.1.7 on 2023-02-22 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0010_car_closed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="doors",
            new_name="doors_count",
        ),
    ]
