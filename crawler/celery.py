from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')

app = Celery('crawler')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    """
    'Import Reviews': {
        'task': 'app.tasks.crawl_app_reviews',
        'schedule': crontab(minute='*/10'),
        'args': ('com.nianticlabs.pokemongo',)
    },
    'Import All Reviews': {
        'task': 'app.tasks.crawl_all_app_reviews',
        'schedule': crontab(hour='*/1'),
        'args': ('com.nianticlabs.pokemongo',)
    },
    """
    'Import App': {
        'task': 'app.tasks.import_app_info',
        'schedule': crontab(minute='*/2'),
        'args': ('com.nianticlabs.pokemongo',)
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Job request: {self.request!r}')
