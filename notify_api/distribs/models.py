from django.db import models


class Distrib(models.Model):
    distrib_id = models.IntegerField()
    distrib_begin_time = models.DateTimeField()
    distrib_end_time = models.DateTimeField()
    ditrib_text = models.CharField(max_length=255)
    distrib_tag = models.CharField(max_length=255)
    distrib_op = models.IntegerField()


    def __str__(self):
        return self.distrib_tag