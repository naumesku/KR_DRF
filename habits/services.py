from datetime import timedelta
import requests
from django.utils import timezone
from config import settings

def time_next_notify_prep(time, period):
    """функция расчета следующего напоминания"""

    time_now = timezone.now().replace(second=0, microsecond=0)
    start_time = time.replace(second=0, microsecond=0)


    if start_time > time_now:
        return start_time
    else:
        return time_next_notify_prep((start_time+timedelta(hours=period)), period)

def send_alarm_to_telegramm(chat_id, action):
    """функция отправки напоминания в телеграмм"""
    URL = settings.URL
    TOKEN = settings.TELEGRAM_API_TOKEN
    response = requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': f'Пришло время выполнить привычку: {action}'
        }
    )
