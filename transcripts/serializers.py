from rest_framework import serializers
from .models import AudioTranscript


class AudioTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioTranscript
        fields = '__all__'
