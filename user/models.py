from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=64)
    creation_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    