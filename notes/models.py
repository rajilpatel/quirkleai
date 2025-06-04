from django.db import models
from django.conf import settings

class TherapyNote(models.Model):
    NOTE_TYPES = (
        ('soap', 'SOAP'),
        ('dap', 'DAP'),
        ('freeform', 'Freeform'),
    )
    session = models.ForeignKey('therapy_sessions.TherapySession', on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note_type = models.CharField(max_length=20, choices=NOTE_TYPES, default='freeform')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.session}: {self.note_type}"
