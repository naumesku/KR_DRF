# Generated by Django 4.2.7 on 2024-03-14 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_remove_habit_start_time_new_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_next_notify',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 22, 29, 27, 289284), verbose_name='Время следующего оповещения'),
        ),
    ]
