from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title