# Generated by Django 4.2.1 on 2023-05-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_task_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_hour',
            field=models.DateTimeField(),
        ),
    ]
