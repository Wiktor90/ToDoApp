from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title