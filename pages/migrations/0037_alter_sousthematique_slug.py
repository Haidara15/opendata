# Generated by Django 5.1.4 on 2025-02-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_alter_sousthematique_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sousthematique',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
