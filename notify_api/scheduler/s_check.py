from celery import shared_task
from datetime import datetime
from distribs.models import Distrib
from s_form_message import form_message

@shared_task
def check():
    now = datetime.now()
    q = Distrib.objects.filter(distrib_begin_time__gte=now, distrib_end_time__lte=now)
    if q:
        for distrib in q:
            form_message.delay(distrib)

