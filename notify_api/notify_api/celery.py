import os
from celery import Celery
# to run the beat:
# $ celery -A notify_api beat -l INFO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notify_api.settings')
app = Celery('notify_api', broker='redis://localhost:6379')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
#scheduled for every 10 seconds app for new distributions
#app in scheduler/s_check.py
app.conf.beat_schedule = {
    'db_checker': {
        'task': 'scheduler.s_check.check',
        'schedule': 10.0
    }
}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')