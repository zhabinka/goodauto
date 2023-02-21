# Generated by Django 4.1.7 on 2023-02-20 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0024_htmlbunchstorage_source_html"),
    ]

    operations = [
        migrations.AddField(
            model_name="urlstorage",
            name="car_model",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="storage.carmodel",
            ),
            preserve_default=False,
        ),
    ]