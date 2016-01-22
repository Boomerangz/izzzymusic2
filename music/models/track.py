__author__ = 'igorzygin'

from django.contrib.auth.models import User
from django.db import models


class Track(models.Model):
    class Meta:
     ordering = ['-id']
	
    artist = models.CharField(max_length=255, default="", blank=True)
    album = models.CharField(max_length=255, default="", blank=True)
    title = models.CharField(max_length=255, default="", blank=True)
    duration = models.IntegerField(max_length=255, default=0, blank=True)
    link = models.CharField(max_length=255, default="", blank=True)
    telegram_id = models.CharField(max_length=255, default="", blank=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.str()

    def str(self):
        return self.artist +" - " +self.title


class Like(models.Model):
    track = models.ForeignKey(Track)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)