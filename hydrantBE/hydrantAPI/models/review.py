from django.db import models
from .hydrant import Hydrant
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=100)
    review_text = models.CharField(max_length=1000, null=True, blank=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    hydrant = models.ForeignKey(Hydrant, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='review_created_by_user', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.title)
