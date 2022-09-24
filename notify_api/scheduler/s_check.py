from celery import shared_task
from datetime import datetime
from distribs.models import Distrib
from s_form_message import form_message

@shared_task
def check():
    now = datetime.now()

    if Distrib.objects.filter(begin_time__gte=now, end_time__lte=now):
        q = Distrib.objects.filter(begin_time__gte=now, end_time__lte=now)
        for distrib in q:
            form_message.delay(id=distrib.id, text=distrib.text, tag=distrib.tag, operator=distrib.operator)