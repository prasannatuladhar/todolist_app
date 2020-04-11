from django.db import models

class TaskList(models.Model):
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task


