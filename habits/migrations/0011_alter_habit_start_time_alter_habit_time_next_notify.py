# Generated by Django 4.2.7 on 2024-03-15 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0010_alter_habit_start_time_alter_habit_time_next_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 17, 36, 12, 981096), verbose_name='время и дата начала привычки'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_next_notify',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 17, 36, 12, 982108), verbose_name='Время следующего оповещения'),
        ),
    ]