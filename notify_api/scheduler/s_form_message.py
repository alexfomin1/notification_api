from celery import shared_task

from clients.models import Client
from s_send import send_request
from mymessages.models import Message


@shared_task
def find_clients(tag, operator):
    return Client.objects.filter(tag=tag, operator=operator)

@shared_task
def form_message(id, text, tag, operator):
    clients = find_clients.delay(tag, operator)
    for client in clients:
        new_message = Message(status='CREATED', text=text, cl_id=client.id, distrib_id=id)
        new_message.save()
        send_request.delay(new_message.id)