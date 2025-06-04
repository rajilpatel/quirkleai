from rest_framework import viewsets, permissions

from .models import TherapySession
from .serializers import TherapySessionSerializer
from .utils import generate_jitsi_room_name

class TherapySessionViewSet(viewsets.ModelViewSet):
    queryset = TherapySession.objects.all()
    serializer_class = TherapySessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        session = serializer.save()
        if not session.room_name:
            session.room_name = generate_jitsi_room_name()
            session.save()
