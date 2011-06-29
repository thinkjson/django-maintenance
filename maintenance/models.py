from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.cache import cache
from django.conf import settings
from datetime import datetime

class MaintenanceMessage(models.Model):
    message = models.TextField()
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.message

# Invalidate the cache when a MaintenanceMessage is saved
@receiver(post_save, sender=MaintenanceMessage)
def invalidate_message_cache(sender, **kwargs):
    if not getattr(settings, 'MAINTENANCE_CACHE_MESSAGES', False):
        cache.delete('maintenance_messages')