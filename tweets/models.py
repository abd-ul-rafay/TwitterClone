from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    hashtags = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
