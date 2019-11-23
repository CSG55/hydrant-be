from django.db import models
from django.contrib.gis.db import models

class Hydrant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    location = models.PointField()
    def __str__(self):
        return self.name
