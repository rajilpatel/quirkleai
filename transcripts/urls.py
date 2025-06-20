from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioTranscriptViewSet

router = DefaultRouter()
router.register(r'transcripts', AudioTranscriptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
