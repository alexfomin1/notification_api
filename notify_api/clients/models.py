from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from tags.models import Tag


class Client(ExportModelOperationsMixin('client'), models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.IntegerField()
    operator = models.IntegerField()
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
    zone = models.CharField(max_length=50)

    def __str__(self):
        return self.zone