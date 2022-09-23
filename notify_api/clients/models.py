from django.db import models


class Client(models.Model):
    client_id = models.IntegerField()
    client_phone = models.IntegerField()
    client_op = models.IntegerField()
    client_tag = models.CharField(max_length=255)
    client_zone = models.CharField(max_length=50)

    def __str__(self):
        return self.client_tag