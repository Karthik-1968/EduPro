# Generated by Django 4.2.16 on 2024-12-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("type_form", "0002_alter_dynamicform_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dynamicform",
            name="id",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
