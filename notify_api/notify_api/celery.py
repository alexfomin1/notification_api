import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notify_api.settings')
app = Celery('notify_api', broker='redis://localhost:6379')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'scheduler.tasks.check',
        'schedule': 10.0,
#        'args': 2
    }
}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')