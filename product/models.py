from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    publish_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
