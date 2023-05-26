from django.db import models

class GroomSide(models.Model):
    name = models.CharField(max_length=100)
    attending_gurdwara_choices = (
        ('yes', 'Accept with Pleasure'),
        ('no', 'Regretfully Decline'),
    )
    attending_gurdwara_groom = models.CharField(max_length=10, choices=attending_gurdwara_choices, null=True)
    total_attending_gurdwara_groom = models.IntegerField(default=0)  # Add default value here
    coach_attending_gurdwara_groom = models.IntegerField(default=0)  # Add default value here
    attending_reception_choices = (
        ('yes', 'Accept with Pleasure'),
        ('no', 'Regretfully Decline'),
    )
    attending_reception_groom = models.CharField(max_length=10, choices=attending_reception_choices, null=True)
    total_attending_reception_groom = models.IntegerField(default=0)  # Add default value here
    coach_attending_reception_groom = models.IntegerField(default=0)  # Add default value here
    song_request_groom = models.TextField(blank=True)

class BrideSide(models.Model):
    name = models.CharField(max_length=100)
    attending_gurdwara_choices = (
        ('yes', 'Accept with Pleasure'),
        ('no', 'Regretfully Decline'),
    )
    attending_gurdwara_bride = models.CharField(max_length=10, choices=attending_gurdwara_choices, null=True)
    total_attending_gurdwara_bride = models.IntegerField(default=0)  # Add default value here
    attending_reception_choices = (
        ('yes', 'Accept with Pleasure'),
        ('no', 'Regretfully Decline'),
    )
    attending_reception_bride = models.CharField(max_length=10, choices=attending_reception_choices, null=True)
    total_attending_reception_bride = models.IntegerField(default=0)  # Add default value here
    song_request_bride = models.TextField(blank=True)