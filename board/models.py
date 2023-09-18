from django.db import models
from team.models import Team

# Create your models here.

class Board(models.Model):
    choices = (
        ("OPEN","OPEN"),
        ("IN_PROGRESS","IN_PROGRESS"),
        ("CLOSED","CLOSED"),
    )
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=choices, default="OPEN")
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Task(models.Model):
    choices = (
        ("OPEN","OPEN"),
        ("IN_PROGRESS","IN_PROGRESS"),
        ("COMPLETE","COMPLETE"),
    )
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=choices, default="OPEN")
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
