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

@shared_task
def send_request(id, phone, text):
    try:
        data = {
            'id': id,
            'phone': phone,
            'text': text
        }
        response = requests.get(f'https://probe.fbrq.cloud/v1/send/{str(id)}', data=data, auth=BearerAuth(os.environ['TOKEN_SERVER']))
        print(response)
    except:
        print('task failed')
    finally:
        print('task finished')