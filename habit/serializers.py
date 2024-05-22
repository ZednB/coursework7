from rest_framework import serializers

from habit.models import Habit
from habit.validators import RewardOrRelatedValidator, TimeValidator, LinkedAndIsPleasantValidator, \
    PleasantHabitValidator, PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardOrRelatedValidator(),
            TimeValidator(),
            LinkedAndIsPleasantValidator(),
            PleasantHabitValidator(),
            PeriodicityValidator()
        ]
