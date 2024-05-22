from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateApiView(generics.CreateAPIView):
    """Контроллер для создания новой привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save(user=self.request.user)
        user.save()


class HabitListApiView(generics.ListAPIView):
    """Контроллер для просмотра списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """Контроллер для просмотра одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(generics.UpdateAPIView):
    """Контроллер для редактирования привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyApiView(generics.DestroyAPIView):
    """Контроллер для удаления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAdminUser, IsOwner]
