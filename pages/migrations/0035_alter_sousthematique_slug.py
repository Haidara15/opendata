# Generated by Django 5.1.4 on 2025-02-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_alter_sousthematique_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sousthematique',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
