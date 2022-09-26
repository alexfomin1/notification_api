from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from clients.models import Client
from tags.models import Tag


class Distrib(ExportModelOperationsMixin('distrib'), models.Model):
    id = models.AutoField(primary_key=True)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    text = models.CharField(max_length=255)
    cl = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text