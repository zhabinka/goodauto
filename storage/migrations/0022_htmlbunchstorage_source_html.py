# Generated by Django 4.1.7 on 2023-02-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0021_remove_urlstorage_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="htmlbunchstorage",
            name="source_html",
            field=models.TextField(blank=True),
        ),
    ]
