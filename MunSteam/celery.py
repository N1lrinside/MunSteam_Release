import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MunSteam.settings')

app = Celery('MunSteam')
app.config_from_object('django.conf.settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_players': {
        'task': 'games.tasks.get_players_in_game',
        'schedule': crontab(minute='*/5')
    },
    'update_time': {
        'task': 'games.tasks.update_time',
        'schedule': crontab(minute='*')
    },
    'update_news': {
        'task': 'games.tasks.get_news_about_game',
        'schedule': crontab(day_of_month='*/3', hour=0, minute=0)
    }
}
