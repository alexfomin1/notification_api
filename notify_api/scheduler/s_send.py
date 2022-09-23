import json
from celery import shared_task
import requests
from pathlib import Path
import os
import dotenv

from .auth_bearer import BearerAuth

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def send_request(self, id, phone, text):
    try:
        data = {
            'id': id,
            'phone': phone,
            'text': text
        }
        response = requests.get(f'https://probe.fbrq.cloud/v1/send/{str(id)}', data=json.dumps(data), auth=BearerAuth(os.environ['TOKEN_SERVER']))
        return response
    except:
        raise Exception()
    finally:
        return 'task finished'