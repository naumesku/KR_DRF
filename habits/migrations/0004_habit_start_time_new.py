# Generated by Django 4.2.7 on 2024-03-14 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_habit_time_next_notify'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='start_time_new',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 17, 47, tzinfo=datetime.timezone.utc), verbose_name='время и дата начала привычки новая'),
        ),
    ]