# Generated by Django 4.1.5 on 2023-02-16 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_create_car"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="car",
            table="cars",
        ),
    ]
