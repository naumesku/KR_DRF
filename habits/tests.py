from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User
from django.urls import reverse


class HabitCRUDTest(APITestCase):
    """Класс проверки механизма CRUD для привычки"""
    def setUp(self) -> None:
        self.user = User.objects.create(email='glav.spb.bars@onlinetrade.ru')
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place='Test place',
            action='Test action',
            period=1,
            execution_time='00:01',
            time="2024-03-17T10:52:50.515434Z",
            user=self.user
        )

    def test_get_list(self):
        """Тест просмотра списка привычек"""
        response = self.client.get(
            reverse('habits:habit-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {"count": 1,
                    "next": None,
                    "previous": None,
                    "results": [
                           {"id": self.habit.id,
                            "period": 1,
                            "place": "Test place",
                            "action": "Test action",
                            "time": "2024-03-17T10:52:50.515434Z",
                            "is_nice": False,
                            "award": None,
                            "execution_time": "00:01:00",
                            "is_public": False,
                            "user": self.user.id,
                            "related_habit": None},
                    ]
                }
            )

    def test_create(self):
        """Тест создания привычки"""

        data = {
                "period": 1,
                "place": "Test place",
                "action": "Test action",
                "time": "2024-03-17T13:48:12.058373Z",
                "execution_time": "00:01",
                "user": self.user.id
            }

        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
                {
                        "id": 2,
                        "period": 1,
                        "place": "Test place",
                        "action": "Test action",
                        "time": "2024-03-17T13:48:12.058373Z",
                        "is_nice": False,
                        "award": None,
                        "execution_time": "00:01:00",
                        "is_public": False,
                        "user": self.user.id,
                        "related_habit": None
                        }
        )

    def test_updaate(self):
        """Тест обновления привычки"""

        habit_update = Habit.objects.all().filter(user_id=self.user).first()
        pk_update = habit_update.id
        data = {"action": "test update",
                "period": 2,
                "time": "2024-03-17T13:48:12.058373Z",
                "execution_time": "00:02"}
        response = self.client.put(
                f'/habits/update/{pk_update}/',
                data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": pk_update,
                "period": 2,
                "place": "Test place",
                "action": "test update",
                "time": "2024-03-17T13:48:12.058373Z",
                "is_nice": False,
                "award": None,
                "execution_time": "00:02:00",
                "is_public": False,
                "user": self.user.id,
                "related_habit": None
            }
        )
    def test_delete(self):
        """Тест удаление привычки"""
        habit_delete = Habit.objects.all().filter(user_id=self.user).first()
        pk_delete = habit_delete.id
        print('pk_delete=', pk_delete)
        response = self.client.delete(
                f'/habits/delete/{pk_delete}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
