from django.db import models


class GroomSide(models.Model):
    name = models.CharField(max_length=100)
    attending_choices = (
        ('yes', 'Accept with Pleasure'),
        ('no', 'Regretfully Decline'),
    )
    attending = models.CharField(max_length=10, choices=attending_choices)
    total_attending = models.IntegerField()
    coach_attending = models.IntegerField()
    song_request = models.CharField(max_length=200, default=None)

class BrideSide(models.Model):
    name = models.CharField(max_length=100)
    attending_choices = (
        ('yes', 'Accept with Pleasure'),
        ('no', 'Regretfully Decline'),
    )
    attending = models.CharField(max_length=10, choices=attending_choices)
    total_attending = models.IntegerField()
    song_request = models.CharField(max_length=200, default=None)


