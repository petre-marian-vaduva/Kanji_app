# yourvenv/cfehome/celery.py
from __future__ import absolute_import, unicode_literals # for python2
from celery import Celery
import os
# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mooch_project.settings')


## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('mooch_project')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')



# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
# app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'



app.conf.beat_schedule = {
    # 'add-every-6-seconds': {
    #     'task': 'sum_two_numbers',
    #     'schedule': 6.0,
    #     'args': (2, 3)
    # },
    'create_log': {
        'task': 'script1',
        'schedule': 10.0
    },
    'change_status': {
        'task': 'script2',
        'schedule': 8.0
    },
}
