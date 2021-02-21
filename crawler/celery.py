from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')

app = Celery('crawler')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'Import App Info': {
        'task': 'app.tasks.crawl_all_app_reviews',
        'schedule': crontab(hour='*/1'),
        'args': ('com.nianticlabs.pokemongo',)
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Job request: {self.request!r}')
