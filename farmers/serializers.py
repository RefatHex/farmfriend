from rest_framework import serializers
from .models import Farmer, FarmerGigs, Crops

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['name', 'picture', 'field_size', 'average_rating']

class FarmerGigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerGigs
        fields = ['title', 'description', 'price']

class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = ['name', 'image']
