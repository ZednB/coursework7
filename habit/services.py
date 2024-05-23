import logging

from config import settings
import requests

logger = logging.getLogger(__name__)


def send_message(chat_id, message):
    params = {
        'chat_id': chat_id,
        'text': message,
    }
    response = requests.post(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
    if response.status_code != 200:
        logger.info(f"fail {response.status_code, response.text}")
    else:
        logger.info(f"success {response.status_code}")
