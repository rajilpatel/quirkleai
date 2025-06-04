from rest_framework import viewsets
from .models import TherapySession
from .serializers import TherapySessionSerializer


class TherapySessionViewSet(viewsets.ModelViewSet):
    queryset = TherapySession.objects.all()
    serializer_class = TherapySessionSerializer
