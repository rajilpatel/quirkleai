from django.db import models


class AudioTranscript(models.Model):
    session = models.ForeignKey('therapy_sessions.TherapySession', on_delete=models.CASCADE)
    file = models.FileField(upload_to='transcripts/')
    text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
