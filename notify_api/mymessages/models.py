from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from clients.models import Client
from distribs.models import Distrib


class Message(ExportModelOperationsMixin('message'), models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    distrib = models.ForeignKey(Distrib, on_delete=models.DO_NOTHING)
    cl = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.status