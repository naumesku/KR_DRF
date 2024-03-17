from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse


class UserCRUDTest(APITestCase):
    """Класс проверки механизма CRUD для привычки"""

    def test_create(self):
        """Тест создания пользователя"""

        data = {
                "email": "prp5@bk.ru",
                "chat_id": "535434467",
                "password": "qwe123rty456",
                "date_joined": "2024-03-17T15:15:38.494647Z",
                }

        response = self.client.post(
            reverse('users:user-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user = User.objects.all().filter(email="prp5@bk.ru").first()
        self.assertEqual(
            response.json(),
            {
                "id": self.user.id,
                "last_login": None,
                "is_superuser": False,
                "first_name": "",
                "last_name": "",
                "is_staff": False,
                "date_joined": "2024-03-17T15:15:38.494647Z",
                "email": "prp5@bk.ru",
                "chat_id": "535434467",
                "avatar": None,
                "phone": None,
                "town": None,
                "is_active": True,
                "groups": [],
                "user_permissions": []
            }
        )


    def test_updaate(self):
        """Тест обновления ползователя"""

        self.user = User.objects.create(email='prp6@bk.ru')
        self.client.force_authenticate(user=self.user)
        data = {
            "last_name": "Тест",
            "chat_id": "535434465",
            "first_name": "Тест",
            "date_joined": "2024-03-17T15:15:38.494647Z",
        }
        response = self.client.patch(
                f'/user/update/{self.user.id}/',
                data=data
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": self.user.id,
                "last_login": None,
                "is_superuser": False,
                "first_name": "Тест",
                "last_name": "Тест",
                "is_staff": False,
                "date_joined": "2024-03-17T15:15:38.494647Z",
                "email": "prp6@bk.ru",
                "chat_id": "535434465",
                "avatar": None,
                "phone": None,
                "town": None,
                "is_active": False,
                "groups": [],
                "user_permissions": []
            }
        )

    def test_delete(self):
        """Тест удаление пользователя"""
        self.user = User.objects.create(email='prp6@bk.ru')
        self.client.force_authenticate(user=self.user)
        pk_delete = self.user.id
        response = self.client.delete(
                f'/user/delete/{pk_delete}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )