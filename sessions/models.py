from django.db import models
from django.conf import settings

class TherapySession(models.Model):
    therapist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='therapist_sessions')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_sessions')
    scheduled_for = models.DateTimeField()
    room_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.client} with {self.therapist} at {self.scheduled_for}"
