# Generated by Django 5.0.3 on 2024-05-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0014_alter_thematiques_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sousthematique",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
