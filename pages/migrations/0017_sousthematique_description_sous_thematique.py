# Generated by Django 5.0.3 on 2024-05-01 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0016_alter_sousthematique_slug_alter_thematiques_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="sousthematique",
            name="description_sous_thematique",
            field=models.TextField(blank=True),
        ),
    ]
