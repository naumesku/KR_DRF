from rest_framework import generics
from rest_framework.permissions import AllowAny
from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitSerializer

class HabitCreateAPIView(generics.CreateAPIView):
    """Представление для создания привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Переопределение метода "создание": сохраняем пользователя в БД"""
        new_habit = serializer.save(user=self.request.user)
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Представление для просмотра всех привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user) | Habit.objects.filter(is_public=True).exclude(user=user)

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра 1 занятия"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user) | Habit.objects.filter(is_public=True).exclude(user=user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Представление для редактирования занятия"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Представление для удаления 1 занятия"""
    queryset = Habit.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)
