# Generated by Django 5.0.3 on 2024-03-24 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thematiques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='static/images')),
                ('date_ajout', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
    ]
