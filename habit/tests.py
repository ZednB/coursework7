from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        """Создание тестового пользователя"""
        self.user = User.objects.create(email='test@mail.ru', password='12345')
        self.client.force_authenticate(user=self.user)
        self.permission = IsAuthenticatedOrReadOnly()

        self.habit = Habit.objects.create(user=self.user,
                                          place='Везде',
                                          time='2024-05-23 21:50:00',
                                          action='Кодить',
                                          is_pleasant=True,
                                          linked_habit=None,
                                          periodicity=7,
                                          reward='Деньги',
                                          duration=30,
                                          is_public=True)

    def test_create_habit(self):
        url = reverse('habit:habit_create')
        """Тест на создание привычки"""
        data = {
            'user': self.user.id,
            'place': 'Везде',
            'time': '2024-05-23|21:20',
            'action': 'Кодить',
            'is_pleasant': True,
            'linked_habit': '',
            'periodicity': 7,
            'reward': None,
            'duration': 30,
            'is_public': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_get_habit(self):
        response = self.client.get('/habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        data = {
            'place': 'Дома',
            'action': 'Играть',
            'duration': 40,
            'time': '2024-05-23|21:20'
        }
        response = self.client.put(f'/habit/update/{self.habit.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve_habit(self):
        data = {
            'place': 'Дома',
            'action': 'Играть',
            'duration': 40,
            'time': '2024-05-23|21:20'
        }
        response = self.client.get(f'/habit/{self.habit.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_habit(self):
        response = self.client.delete(f'/habit/delete/{self.habit.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
