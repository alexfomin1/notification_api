from celery import shared_task

from s_send import send_request
from mymessages.models import Message


@shared_task
def create_message(id, text):
    Message.objects.create(status='CREATED', text=text, id=id)

@shared_task
def find_clients(tag, operator):
    pass

@shared_task
def update_status(status):
    pass

@shared_task
def form_message(id, text, tag, operator):
    create_message.delay(id, text)
    clients = find_clients.delay(tag, operator)

    for client in clients:
        send_request.delay(client.id, client.phone, text)