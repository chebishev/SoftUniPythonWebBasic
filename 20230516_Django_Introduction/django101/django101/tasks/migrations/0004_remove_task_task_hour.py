# Generated by Django 4.2.1 on 2023-05-17 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_task_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_hour',
        ),
    ]
