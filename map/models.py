from django.db import models


# Create your models here.

class Sheep(models.Model):
    serial = models.CharField(max_length=128, blank=False)
    lastLocationUpdate = models.DateTimeField()
    lastKnownLat = models.FloatField()
    lastKnownLng = models.FloatField()
