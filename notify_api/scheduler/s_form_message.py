from celery import shared_task

from s_send import send_request


@shared_task
def form_message(q):
    id = 0
    phone = 0
    text = 0
    send_request.delay(id, phone, text)