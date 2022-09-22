from django.db import models


class Message(models.Model):
    message_id = models.CharField(max_length=255, unique=True)
    message_time = models.DateTimeField(auto_now_add=True)
    message_status = models.CharField(max_length=255)
    message_distrib_id = models.CharField(max_length=255)
    message_client_id = models.CharField(max_length=255)

    def __str__(self):
        return self.message_id