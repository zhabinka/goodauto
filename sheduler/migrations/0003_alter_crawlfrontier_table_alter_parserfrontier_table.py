# Generated by Django 4.1.7 on 2023-02-17 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sheduler", "0002_create_parser_frontier"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="crawlfrontier",
            table="crawl_frontier",
        ),
        migrations.AlterModelTable(
            name="parserfrontier",
            table="parser_frontier",
        ),
    ]
