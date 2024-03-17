from celery import shared_task
from habits.models import Habit
from habits.services import time_next_notify_prep, send_alarm_to_telegramm
from users.models import User
from django.utils import timezone

@shared_task
def send_alarm():
    """функция готовит напоминания и отправляет уведомления о необходимости выполнить привычку"""
    print('Работает send_alarm')
    datetime_now = timezone.now().replace(second=0, microsecond=0)

    habits_expired_notify = Habit.objects.filter(
        time__lt=datetime_now
    )
    for habit in habits_expired_notify:
        habit.time = time_next_notify_prep(habit.__dict__['time'], habit.__dict__['period'])
        habit.save()

    habits = Habit.objects.filter(
        time=datetime_now
    )

    for habit in habits:
        users = User.objects.filter(id=habit.user_id)
        for user in users:
            send_alarm_to_telegramm(user.chat_id, habit.action)
