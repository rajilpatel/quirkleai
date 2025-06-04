from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AudioTranscript
from .serializers import AudioTranscriptSerializer
from .utils import transcribe_audio, summarize_transcript

class AudioTranscriptViewSet(viewsets.ModelViewSet):
    queryset = AudioTranscript.objects.all()
    serializer_class = AudioTranscriptSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        transcript = self.get_object()
        transcript.text = transcribe_audio(transcript.audio_file.path)
        transcript.summary = summarize_transcript(transcript.text)
        transcript.save()
        return Response(AudioTranscriptSerializer(transcript).data)
