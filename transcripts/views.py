from rest_framework import viewsets
from .models import AudioTranscript
from .serializers import AudioTranscriptSerializer


class AudioTranscriptViewSet(viewsets.ModelViewSet):
    queryset = AudioTranscript.objects.all()
    serializer_class = AudioTranscriptSerializer
