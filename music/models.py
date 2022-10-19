from abc import update_abstractmethods
from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    album_cover = models.FileField(null=True, blank=True)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    song_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    album_cover = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Playlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=50)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
