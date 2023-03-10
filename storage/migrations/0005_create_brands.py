# Generated by Django 4.1.5 on 2023-02-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0004_create_providers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("manufacturer", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "brands",
                "unique_together": {("manufacturer", "model")},
            },
        ),
    ]
