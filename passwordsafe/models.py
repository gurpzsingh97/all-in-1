from django.db import models
from django.contrib.auth.models import User


PLATFORM_CHOICES = (
    ('Facebook','Facebook'),
    ('Amazon', 'Amazon'),
    ('YouTube','YouTube'),
    ('Instagram','Instagram'),
    ('Google','Google'),
)
class PasswordSafe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='google')
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)


