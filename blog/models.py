from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    post_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pubdate_pretty(self):
        return self.pubdate.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
