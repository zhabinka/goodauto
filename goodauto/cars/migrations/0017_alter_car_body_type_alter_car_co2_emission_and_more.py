# Generated by Django 4.1.7 on 2023-03-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0016_alter_car_html_storage_alter_car_url_storage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="body_type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="co2_emission",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="coc",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="engine_size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="first_registration",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="four_wheel_drive",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="fuel_type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="interior_colour",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="paint",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="power",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="registration_documents",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="vat",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
