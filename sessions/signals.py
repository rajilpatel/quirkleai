from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TherapySession
from notifications.models import Notification

@receiver(post_save, sender=TherapySession)
def session_created(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.client,
            message=f"Session scheduled with {instance.therapist} at {instance.scheduled_for}",
        )
