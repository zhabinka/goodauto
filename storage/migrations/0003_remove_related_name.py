# Generated by Django 4.1.5 on 2023-02-10 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0002_create_html_storage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="htmlstorage",
            name="url_storage",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="storage.urlstorage"
            ),
        ),
    ]
