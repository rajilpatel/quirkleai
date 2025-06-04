from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TherapyNoteViewSet

router = DefaultRouter()
router.register(r'notes', TherapyNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
