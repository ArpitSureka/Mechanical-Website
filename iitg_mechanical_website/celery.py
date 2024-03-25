from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iitg_mechanical_website.settings.base') # project name.settings

app = Celery('iitg_mechanical_website') # provide your project name
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app.conf.beat_schedule = {
# create an object for your scheduling your task
    'fetch-and-store-temp-data-contrab': {
        'task': 'apilist.tasks.fetch_and_store_temperature', #app_name.tasks.function_name
        'schedule': crontab(minute='*/15'), #crontab() means run every minute
        # 'args' : (..., ...) In case function takes parameters, add them here
    }
}