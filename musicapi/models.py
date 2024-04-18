from django.db import models
from datetime import datetime
# Create your models here.

class HitMusicModel(models.Model):
    track = models.FileField(upload_to='tracks/')
    track_name = models.CharField(max_length=25)
    track_image = models.ImageField(upload_to='images/')
    track_author = models.CharField(blank=True,null=True,max_length=25)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.track_name