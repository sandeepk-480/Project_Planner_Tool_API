from django.db import models
from user.models import User

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    users = models.ManyToManyField(User, help_text="Team members list")

    def __str__(self):
        return self.name
