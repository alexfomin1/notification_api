from celery import shared_task
from datetime import datetime
from distribs.models import Distrib
from s_form_message import form_message
import logging


@shared_task
def check():
    logger = logging.getLogger('main')
    logger.info('checking dates')
    now = datetime.now()

    if Distrib.objects.filter(begin_time__gte=now, end_time__lte=now):
        logger.info('distribs found')
        q = Distrib.objects.filter(begin_time__gte=now, end_time__lte=now)
        for distrib in q:
            logger.info('forming ditribs')
            form_message.delay(id=distrib.id, text=distrib.text, tag=distrib.tag, operator=distrib.operator)