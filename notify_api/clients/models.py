from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Client(ExportModelOperationsMixin('client'), models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.IntegerField()
    operator = models.IntegerField()
    tag = models.CharField(max_length=255)
    zone = models.CharField(max_length=50)

    def __str__(self):
        return self.tag