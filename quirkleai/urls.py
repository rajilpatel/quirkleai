from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from therapy_sessions.views import TherapySessionViewSet
from notes.views import TherapyNoteViewSet
from transcripts.views import AudioTranscriptViewSet
from notifications.views import NotificationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sessions', TherapySessionViewSet)
router.register(r'notes', TherapyNoteViewSet)
router.register(r'transcripts', AudioTranscriptViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
