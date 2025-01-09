from rest_framework import serializers
from .models import Farmer, FarmerGigs, Crops

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['user', 'name', 'picture', 'dob', 'address', 'field_size', 'average_rating']


class FarmerGigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerGigs
        fields = ['farmer','title', 'description', 'price', 'quantity']

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value


class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = ['farmer','name', 'image']
