# Generated by Django 4.2.16 on 2025-01-10 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0006_remove_item_emis_remove_item_exchangeproperties_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="items",
        ),
        migrations.RemoveField(
            model_name="whishlist",
            name="items",
        ),
    ]
