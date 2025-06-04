from rest_framework import serializers
from .models import AudioTranscript

class AudioTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioTranscript
        fields = ['id', 'session', 'audio_file', 'text', 'summary', 'created']
        read_only_fields = ['text', 'summary', 'created']
