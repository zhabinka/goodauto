# Generated by Django 4.1.7 on 2023-02-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sheduler", "0005_alter_crawlerfrontier_table_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="crawlerfrontier",
            name="type_url",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "single"), (2, "bunch")], default=1
            ),
        ),
        migrations.AddField(
            model_name="parserfrontier",
            name="type_url",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "single"), (2, "bunch")], default=1
            ),
        ),
    ]
