# Generated by Django 4.2.2 on 2023-06-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('ingredients', models.CharField(max_length=250)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
