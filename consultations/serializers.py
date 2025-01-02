from rest_framework import serializers
from .models import Agronomist, ConsultationRequest

class AgronomistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agronomist
        fields = ['name', 'picture', 'specialty', 'years_of_experience', 'availability']

class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRequest
        fields = ['farmer', 'agronomist', 'request_date', 'status', 'details']
