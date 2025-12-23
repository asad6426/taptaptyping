from django.db import models
from datetime import datetime
from django.utils import timezone
from tinymce.models import HTMLField
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    posted_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)  # New image field

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    posted_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # New image field

    def __str__(self):
        return self.title