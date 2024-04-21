from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=125)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=125, blank=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
