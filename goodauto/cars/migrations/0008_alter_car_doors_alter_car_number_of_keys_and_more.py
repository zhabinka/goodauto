# Generated by Django 4.1.7 on 2023-02-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0007_alter_car_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="doors",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="number_of_keys",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="number_of_seats",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
