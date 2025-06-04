from rest_framework import serializers
from .models import TherapyNote


class TherapyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyNote
        fields = '__all__'
