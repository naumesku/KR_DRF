# Generated by Django 4.2.7 on 2024-03-13 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='место')),
                ('action', models.CharField(max_length=200, verbose_name='действие')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='время и дата начала привычки')),
                ('is_nice', models.BooleanField(default=False, verbose_name='приятная привычка')),
                ('period_choices', models.PositiveIntegerField(default=24, verbose_name='периодичность')),
                ('award', models.CharField(blank=True, max_length=200, null=True, verbose_name='вознаграждение')),
                ('execution_time', models.TimeField(verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная приычка')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
            ],
        ),
    ]
