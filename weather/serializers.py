from rest_framework import serializers
from .models import WeatherUpdate

class WeatherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherUpdate
        fields = '__all__'
