from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    priorities = models.IntegerField(default=3)
    status = models.CharField(max_length=20)
    due_date = models.DateTimeField()