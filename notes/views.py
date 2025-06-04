from rest_framework import viewsets
from .models import TherapyNote
from .serializers import TherapyNoteSerializer


class TherapyNoteViewSet(viewsets.ModelViewSet):
    queryset = TherapyNote.objects.all()
    serializer_class = TherapyNoteSerializer
