from django.core.validators import MaxValueValidator
from rest_framework import serializers
from habits.models import Habit
from habits.validators import Execution_time_Validator, OnlyOneFieldValidator, Habit_is_related_validator, \
    Habit_is_nice_validator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для Привычки"""
    period = serializers.IntegerField(validators=[MaxValueValidator(168)])

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            Execution_time_Validator(field='execution_time'),
            Habit_is_nice_validator(),
            OnlyOneFieldValidator(),
            Habit_is_related_validator(field='related_habit'),
        ]
