from django.db import models
from django.utils import timezone

class New(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.ipg')
    date = models.DateTimeField(default=timezone.now)

