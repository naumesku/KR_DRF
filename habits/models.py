from django.db import models
from conf_my import NULLABLE
from config.settings import AUTH_USER_MODEL
from users.models import User
from django.utils import timezone

# Create your models here.
class Habit(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, **NULLABLE, verbose_name='место')
    action = models.CharField(max_length=200, verbose_name='действие')
    time = models.DateTimeField(default=timezone.now, verbose_name='время привычки')
    is_nice = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    period = models.PositiveIntegerField(default=24, verbose_name='периодичность')
    award = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    execution_time = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='публичная приычка')
