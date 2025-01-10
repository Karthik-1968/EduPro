# Generated by Django 4.2.16 on 2025-01-10 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0005_alter_item_properties"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="emis",
        ),
        migrations.RemoveField(
            model_name="item",
            name="exchangeproperties",
        ),
        migrations.RemoveField(
            model_name="item",
            name="offers",
        ),
        migrations.RemoveField(
            model_name="item",
            name="properties",
        ),
        migrations.RemoveField(
            model_name="item",
            name="warranties",
        ),
        migrations.AlterField(
            model_name="itemproperty",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="itemproperties",
                to="amazon.item",
            ),
        ),
        migrations.AlterField(
            model_name="itemproperty",
            name="property",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="itemproperties",
                to="amazon.property",
            ),
        ),
    ]
