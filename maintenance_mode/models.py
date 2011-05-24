from django.db import models
from datetime import datetime

class MaintenanceMessage(models.Model):
    message = models.TextField()
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.message