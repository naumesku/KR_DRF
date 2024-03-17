from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Представление для создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Переопределение метода "создание": делаем зарегистрированных пользователей активными"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UserUpdateAPIView(generics.UpdateAPIView):
    """Представление для редактирования пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    """Представление для удаления 1 пользователя"""
    queryset = User.objects.all()

