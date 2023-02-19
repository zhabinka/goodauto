# Generated by Django 4.1.7 on 2023-02-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0015_alter_htmlstorage_url_storage"),
        ("cars", "0002_rename_cars_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="html_storage",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="html",
                to="storage.htmlstorage",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="url_storage",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="url",
                to="storage.urlstorage",
            ),
        ),
    ]
