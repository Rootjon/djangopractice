from django.db import models

# Create your models here.

class Album (models.Model):
    thumbnail = models.ImageField(upload_to='album/photo')
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)