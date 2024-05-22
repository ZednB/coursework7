from rest_framework import generics

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListApiView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveApiView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyApiView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

