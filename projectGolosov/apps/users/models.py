from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default=' ')
    isCandit = models.BooleanField(default=False)
    candidaterm = models.OneToOneField('golosApp.CanditeForm', null=True, blank=True, on_delete=models.CASCADE)