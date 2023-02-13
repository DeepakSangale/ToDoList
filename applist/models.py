from django.db import models
from django.utils import timezone

# Create your models here.

class ModelClass(models.Model):
    task_name=models.CharField(max_length=100)
    datetime=models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return f'task is {self.task_name} and date time is {self.datetime}'
    