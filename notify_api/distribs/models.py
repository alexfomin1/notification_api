from django.db import models


class Distrib(models.Model):
    id = models.AutoField(primary_key=True)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    text = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    operator = models.IntegerField()


    def __str__(self):
        return self.text