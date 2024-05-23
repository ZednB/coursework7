import logging
from datetime import timedelta, datetime

from celery import shared_task
from django.utils import timezone

from habit.models import Habit
from habit.services import send_message

logger = logging.getLogger(__name__)


@shared_task
def send_note():
    logger.info('Starting task')
    time_now = timezone.now()
    habits = Habit.objects.all()
    logger.info(f'{time_now} - {habits.count()}')
    for habit in habits:
        if habit.time >= time_now - timedelta(minutes=10):
            message = (f"Не забудьте через 10 минут выполнить {habit.action}\n"
                       f"После этого {habit.habits if habit.habits else habit.reward}")
            send_message(chat_id=habit.user.tg_id, message=message)
            logger.info(f'{habit.user.tg_id}: {message}')
            print(logger.info(f'{habit.user.tg_id}: {message}'))
