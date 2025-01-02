from rest_framework import serializers
from .models import RecAIResponse, FertAIResponse

class RecAIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecAIResponse
        fields = '__all__'

class FertAIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FertAIResponse
        fields = '__all__'
