from rest_framework import viewsets, permissions

from .models import TherapyNote
from .serializers import TherapyNoteSerializer

class TherapyNoteViewSet(viewsets.ModelViewSet):
    queryset = TherapyNote.objects.all()
    serializer_class = TherapyNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
