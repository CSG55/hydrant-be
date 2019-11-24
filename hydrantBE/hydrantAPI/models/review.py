from django.db import models
from .hydrant import Hydrant


class Review(models.Model):
    created_by = models.CharField(max_length=100)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    hydrant = models.ForeignKey(Hydrant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
