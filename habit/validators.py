from rest_framework.exceptions import ValidationError


class RewardOrRelatedValidator:
    def __call__(self, habit):
        if habit.get('reward') and habit.get('linked_habit'):
            raise ValidationError(
                "Нельзя одновременно заполнить поля 'Вознаграждение' и 'Связанная привычка'."
            )


class TimeValidator:
    def __call__(self, habit):
        if habit.get('duration') > 120:
            raise ValidationError(
                "Время на выполение должно быть не больше 120 секунд."
            )


class LinkedAndIsPleasantValidator:
    def __call__(self, habit):
        if habit.get('linked_habit') and not habit.get('is_pleasant'):
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class PleasantHabitValidator:
    def __call__(self, habit):
        if habit.get('is_pleasant') and (habit.get('reward') or habit.get('linked_habit')):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )


class PeriodicityValidator:
    def __call__(self, habit):
        if habit.get('periodicity') is not None and habit.get('periodicity') > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
