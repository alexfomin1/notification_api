import json
import logging

from celery import shared_task
import requests
from pathlib import Path
import os
import dotenv

from mymessages.models import Message
from .auth_bearer import BearerAuth

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def send_request(self, id):
    try:
        logger = logging.getLogger('main')
        message = Message.objects.get(id=id)
        data = {
            'id': message.id,
            'phone': message.cl_phone,
            'text': message.text
        }
        logger.info('request formed')
        message.status = 'SENDING'
        message.save()
        response = requests.get(f'https://probe.fbrq.cloud/v1/send/{str(message.id)}', data=json.dumps(data), auth=BearerAuth(os.environ['TOKEN_SERVER']))
        logger.info('waiting for a response')
        return response
    except:
        logger = logging.getLogger('main')
        message = Message.objects.get(id=id)
        message.status = 'ERROR'
        logger.warning('error')
        raise Exception()
    finally:
        logger = logging.getLogger('main')
        message = Message.objects.get(id=id)
        message.status = 'SENT'
        logger.info('message sent')
        return 'task finished'