from django.db import models

class Hydrant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    long = models.FloatField()
    lat = models.FloatField()
    def __str__(self):
        return self.name
