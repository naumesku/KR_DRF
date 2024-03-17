from datetime import timezone, datetime
from rest_framework.serializers import ValidationError


class Execution_time_Validator:
    """Проверяет поле на количество введенных секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        time_obj = datetime.strptime(str(tmp_value), '%H:%M:%S')
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        if not 1 <= total_seconds <= 120:
            raise ValidationError('Время на выполнение должно быть от 1 до 120 секунд')

class OnlyOneFieldValidator:
    """Проверяет попытку заполнения двух полей related_habit и award одвоременно"""

    def __call__(self, attrs):
        field1 = attrs.get('related_habit')
        field2 = attrs.get('award')

        if field1 and field2:
            raise ValidationError("Only one of related_habit or award can be filled")


class Habit_is_nice_validator:
    """Проверяет приятную привычку на наличие вознагрождений или связанной привыки"""

    def __call__(self, attrs):
        is_nice = attrs.get('is_nice')
        award = attrs.get('award')
        related_habit = attrs.get('related_habit')

        if is_nice and (award or related_habit):
            raise ValidationError("Nice_habit can't have award or related_habit")

class Habit_is_related_validator:
    """Проверяет является ли связанная привычка приятной"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_obj = dict(value).get(self.field)
        if habit_obj != None:
            if not habit_obj.__dict__['is_nice']:
                raise ValidationError("related_habit can be only is_nice")
