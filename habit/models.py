from django.db import models
from .validators import (
    RewardOrRelatedValidator,
    TimeValidator,
    LinkedAndIsPleasantValidator,
    PleasantHabitValidator,
    PeriodicityValidator
)

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='habits', **NULLABLE)
    place = models.CharField(max_length=250, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=250, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    linked_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                     related_name='linked_habits')
    periodicity = models.IntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=250, **NULLABLE, verbose_name='Вознаграждение')
    duration = models.PositiveIntegerField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f"{self.user} - {self.action}, {self.place}"

    def clean(self):
        validators = [
            RewardOrRelatedValidator(),
            TimeValidator(),
            LinkedAndIsPleasantValidator(),
            PleasantHabitValidator(),
            PeriodicityValidator()
        ]
        for validator in validators:
            validator(self)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
