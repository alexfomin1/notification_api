from celery import shared_task


@shared_task
def check():
    a = 4 ** 2
    return a