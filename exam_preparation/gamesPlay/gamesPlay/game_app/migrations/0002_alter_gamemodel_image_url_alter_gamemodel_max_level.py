# Generated by Django 4.2.2 on 2023-06-14 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='max_level',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Max Level'),
        ),
    ]
