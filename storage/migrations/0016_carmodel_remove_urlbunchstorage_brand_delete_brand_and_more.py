# Generated by Django 4.1.7 on 2023-02-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0015_alter_htmlstorage_url_storage"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarModel",
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
                ("brand", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "car_models",
                "unique_together": {("brand", "model")},
            },
        ),
        migrations.RemoveField(
            model_name="urlbunchstorage",
            name="brand",
        ),
        migrations.DeleteModel(
            name="Brand",
        ),
        migrations.AddField(
            model_name="urlbunchstorage",
            name="car_model",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="storage.carmodel",
            ),
        ),
    ]
