from django.db import models
from django.conf import settings


class TherapyNote(models.Model):
    NOTE_CHOICES = (
        ('soap', 'SOAP'),
        ('dap', 'DAP'),
        ('freeform', 'Freeform'),
    )
    session = models.ForeignKey('therapy_sessions.TherapySession', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note_type = models.CharField(max_length=20, choices=NOTE_CHOICES, default='freeform')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.note_type} note by {self.author}"
