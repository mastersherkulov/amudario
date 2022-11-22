from __future__ import absolute_import, unicode_literals

import os
from amudario.settings import INSTALLED_APPS
from celery import Celery
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amudario.settings')

app = Celery('amudario', broker_url='redis://127.0.0.1:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(INSTALLED_APPS)


from celery.schedules import crontab

app.conf.beat_schedule = {
    'minut60': {
        'task': 'amudario.tasks.aqiwgtvalue_to_telegram_post',
        'schedule': 60.0,
    },
}