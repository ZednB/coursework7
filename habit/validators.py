from rest_framework.exceptions import ValidationError


class RewardOrRelatedValidator:
    def __call__(self, habit):
        if habit.reward and habit.linked_habit:
            raise ValidationError(
                "Нельзя одновременно заполнить поля 'Вознаграждение' и 'Связанная привычка'."
            )


class TimeValidator:
    def __call__(self, habit):
        if habit.duration > 120:
            raise ValidationError(
                "Время на выполение должно быть не больше 120 секунд."
            )


class LinkedAndIsPleasantValidator:
    def __call__(self, habit):
        if habit.linked_habit and not habit.is_pleasant:
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class PleasantHabitValidator:
    def __call__(self, habit):
        if habit.is_pleasant and (habit.reward or habit.linked_habit):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )


class PeriodicityValidator:
    def __call__(self, habit):
        if habit.periodicity > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
