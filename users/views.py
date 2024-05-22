from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    """Контроллер для регистрации нового пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserListApiView(generics.ListAPIView):
    """Контроллер для просмотра списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRetrieveApiView(generics.RetrieveAPIView):
    """Контроллер для просмотра одного пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsOwner]


class UserUpdateApiView(generics.UpdateAPIView):
    """Контроллер для редактирования пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


class UserDestroyApiView(generics.DestroyAPIView):
    """Контроллер для удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsOwner]
