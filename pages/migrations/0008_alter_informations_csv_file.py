# Generated by Django 5.0.3 on 2024-04-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0007_informations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="informations",
            name="csv_file",
            field=models.FileField(upload_to="csv_files", verbose_name="CSV File"),
        ),
    ]
