from django.db import models
from django.conf import settings

class AudioTranscript(models.Model):
    session = models.ForeignKey('therapy_sessions.TherapySession', on_delete=models.CASCADE, related_name='transcripts')
    audio_file = models.FileField(upload_to='audio/')
    text = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript for {self.session}"
