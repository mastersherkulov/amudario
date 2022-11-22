# Create your tasks here

from celery.schedules import crontab
from celery import shared_task
from amudario.bot import telegram_post 

@shared_task
def aqiwgtvalue_to_telegram_post():
    telegram_post()


