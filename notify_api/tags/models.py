from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Tag(ExportModelOperationsMixin('tag'), models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name