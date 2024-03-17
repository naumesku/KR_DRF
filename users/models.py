from django.contrib.auth.models import AbstractUser
from django.db import models
from conf_my import NULLABLE


class User(AbstractUser):
    """Модель класса User"""

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    chat_id = models.CharField(max_length=30, verbose_name='телеграм токен')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    town = models.CharField(max_length=30, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активация пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} {self.last_login}'

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
