# Generated by Django 4.2.16 on 2024-12-23 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("type_form", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dynamicform",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="forms",
                to="type_form.user",
            ),
        ),
    ]