# Generated by Django 4.1.7 on 2023-02-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0012_rename_number_of_keys_car_keys_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="equipment",
            field=models.TextField(blank=True, null=True),
        ),
    ]