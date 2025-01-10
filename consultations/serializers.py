from rest_framework import serializers
from .models import Agronomist, ConsultationRequest

class AgronomistSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False) 

    class Meta:
        model = Agronomist
        fields = [
            'id', 'user', 'name', 'picture', 'dob', 'contact',
            'address', 'specialty', 'years_of_experience', 'availability'
        ]

class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRequest
        fields = [
            'id', 'farmer', 'agronomist', 'request_date', 'status',
            'details', 'resolution'
        ]
