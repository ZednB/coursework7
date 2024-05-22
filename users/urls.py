from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView, UserDestroyApiView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register_user'),
    path('user/', UserListApiView.as_view(), name='list_user'),
    path('profile/<int:pk>/', UserRetrieveApiView.as_view(), name='profile_user'),
    path('update/<int:pk>/', UserUpdateApiView.as_view(), name='update_user'),
    path('destroy/<int:pk>/', UserDestroyApiView.as_view(), name='destroy_user'),
    ]
