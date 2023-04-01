from django.db import models

class Girl(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attending = models.BooleanField(default=False)
    song_request = models.CharField(max_length=100, blank=True)


class Boy(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attending = models.BooleanField(default=False)
    song_request = models.CharField(max_length=100, blank=True)

