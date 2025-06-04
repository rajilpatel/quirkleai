from rest_framework import serializers
from .models import TherapyNote

class TherapyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyNote
        fields = ['id', 'session', 'author', 'note_type', 'content', 'created', 'updated']
        read_only_fields = ['author', 'created', 'updated']
