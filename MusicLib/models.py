from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField("Artist's name",max_length=100)
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField("Album title ",max_length=100)
    Artist = models.ForeignKey(Artist,on_delete=models.CASCADE )

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField('Track name',max_length=100)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    track_len = models.DurationField('Track length')
    rating = models.IntegerField('User rating')

    def __str__(self):
        return self.title




