# Generated by Django 4.1.7 on 2023-02-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0014_rename_type_url_urlstorage_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="htmlstorage",
            name="url_storage",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="storage.urlstorage"
            ),
        ),
    ]
