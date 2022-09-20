from django.db import models

class Client(models.Model):
    client_id = models.IntegerField()
    phone = models.IntegerField()
    operator_id = models.IntegerField()
    client_tag = models.CharField(max_length=255)
    client_timezone = models.CharField(max_length=255)

    def __str__(self):
        return self.client_id


class Message(models.Model):
    pass


class Mailing(models.Model):
    pass

